from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
	username = forms.CharField(max_length=30, required=True, help_text='Required')
	firstname = forms.CharField(max_length = 30, required=False, help_text='Optional')
	lastname = forms.CharField(max_length=30, required = False, help_text='Optional')
	email = forms.EmailField(max_length=254, required = False, help_text = 'Optional')

	class Meta:
		model = User
		fields = ('username', 'firstname', 'lastname', 'password1', 'password2', 'email')

class LoginForm(forms.Form):
	username = forms.CharField(max_length=30, required=True, help_text='Required')
	password = forms.CharField(widget=forms.PasswordInput(), max_length=30, required=True, help_text='Required')
	
