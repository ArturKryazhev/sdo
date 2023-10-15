from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class SingUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50,help_text='Имя')
    second_name = forms.CharField(max_length=50, help_text='Фамилия')
    e_mail = forms.EmailField(help_text='Электронная почта')
    
    
    class Meta:
        model = User
        fields = ('first_name','second_name','e_mail','password1','password2')
    