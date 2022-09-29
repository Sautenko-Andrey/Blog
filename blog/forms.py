from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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
        if self.__RELEVANT_LENGTH[0] > len(title) or len(title) > self.__RELEVANT_LENGTH[1]:
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


class RegistrationForm(UserCreationForm):

    __USERNAME_LENGTH=(3,15)
    __PASSWORD_LENGTH=(5,15)

    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повторить пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def clean_username(self):
        username=self.cleaned_data['username']
        if len(username)>self.__USERNAME_LENGTH[1] or len(username)<self.__USERNAME_LENGTH[0]:
            raise ValidationError('Логин должен быть не менее, чем из 3 символов и не более 15 символов!')
        return username

    def clean_password1(self):
        password1=self.cleaned_data['password1']
        if len(password1)>self.__PASSWORD_LENGTH[1] or len(password1)<self.__PASSWORD_LENGTH[0]:
            raise ValidationError('Пароль должен быть длиннее 5 символов и короче 15.')
        return password1

    def clean_password2(self):
        password2=self.cleaned_data['password2']
        if password2!=self.password1:
            raise ValidationError('Пароли не совпадают!Проверьте правильность ввода.')
        return password2

