from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfileInfo
from django.contrib.auth.models import User
import uuid


class SignUpForm(UserCreationForm):
    # user_id = forms.IntegerField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    email = forms.EmailField(max_length=32, help_text='Required. Inform a valid email address.',)
    password = forms.CharField(required=True, label='Password', max_length=32, widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'birth_date',  'password1', 'password2', )

class LoginForm(AuthenticationForm):
    user_id = forms.CharField(max_length=10)
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=32, help_text='Required',)
    password = forms.CharField(required=True, label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


