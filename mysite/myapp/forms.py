from django.contrib.auth import authenticate
from django import forms
from django.core.exceptions import ValidationError
from .models import MyUser


class Login(forms.Form):
    username = forms.CharField(label='Your MyUser name', max_length=150)
    password = forms.CharField(label='Your password', widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            self.user = authenticate(username=username, password=password)
            if self.user is None:
                self.add_error(None, 'Username or password incorrect')

# class AuthenticationForm(forms.Form):
#     username = forms.CharField(max_length=254)
#     password = forms.CharField(label="Password", widget=forms.PasswordInput)
#
#     def clean(self):
#         cleaned_data = super().clean()
#         username = cleaned_data.get('username')
#         password = cleaned_data.get('password')
#         self.MyUser = authenticate(username=username, password=password)
#         if self.MyUser is None:
#             raise forms.ValidationError('Не правильный логин/пароль')


class MyForm(forms.Form):
    GENDER = (
        (1, 'Male'),
        (2, 'Female'))
    ENGLISH = (
        (1, 'A1'),
        (2, 'A2'),
        (3, 'B1'),
        (4, 'B2'),
        (5, 'C1'),
        (6, 'C2'))

    name = forms.CharField(label='Name', max_length=100)
    age = forms.IntegerField(label='Age')
    gender = forms.ChoiceField(choices=GENDER)
    english = forms.ChoiceField(choices=ENGLISH)

    def clean(self):
        cleaned_data = super().clean()
        if not (cleaned_data.get('gender') == '1' and cleaned_data.get('age') >= 20
                and int(cleaned_data.get('english')) >= 4) and not (
                cleaned_data.get('gender') == '2' and cleaned_data.get('age') >= 22 and int(cleaned_data.get('english'))
                >= 3):
            raise ValidationError('Error')
