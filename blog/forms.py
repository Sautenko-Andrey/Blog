from django import forms
from .models import *

class WriteToAutorForm(forms.Form):
    title=forms.CharField(max_length=255,label='Тема',
                          required=False,widget=forms.TextInput(attrs={'class':'form-input'}))
    message=forms.CharField(widget=forms.Textarea(attrs={'col':10,'rows':10}),label='Сообщение')
    email=forms.EmailField(max_length=50,label='Email')

