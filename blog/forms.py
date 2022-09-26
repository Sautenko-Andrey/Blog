from django import forms
from django.core.exceptions import ValidationError

from .models import *


class WriteToAutorForm(forms.ModelForm):
    __RELEVANT_LENGTH = (4, 30)
    __FORBIDDEN_EMAIL = '.ru'
    __MIN_MESSAGE_LENGTH = 10

    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-input'}),
        'message': forms.Textarea(attrs={'cols': 50, 'rows': 8}),
    }

    class Meta:
        model = WriteToAutor
        fields = ['title', 'message', 'email']

    def clean_title(self):
        title = self.cleaned_data['title']
        if self.__RELEVANT_LENGTH[0] > len(title) or len(title)>self.__RELEVANT_LENGTH[1]:
            raise ValidationError('Некорректная длина темы сообщения!')
        return title

    def clean_message(self):
        message = self.cleaned_data['message']
        if len(message) < self.__MIN_MESSAGE_LENGTH:
            raise ValidationError('Слишком короткое сообщение!')
        return message

    def clean_email(self):
        email = self.cleaned_data['email']
        if email[-3:] == self.__FORBIDDEN_EMAIL:
            raise ValidationError('Вы не можете зарегестрироваться с такой почтой!')
        return email
