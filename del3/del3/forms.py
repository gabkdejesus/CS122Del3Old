from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from customers.models import Customer
from agents.models import Agent


class SignUpForm(UserCreationForm):
	username = forms.CharField(max_length=30, required=True, help_text='Required')
	firstname = forms.CharField(max_length = 30, required=False, help_text='Optional')
	lastname = forms.CharField(max_length=30, required = False, help_text='Optional')
	email = forms.EmailField(max_length=254, required = False, help_text = 'Optional')
	# agentid = forms.CharField(max_length=255, required=False)
	agentid = forms.ModelChoiceField(queryset=Agent.objects.all())
	street = forms.CharField(max_length=255, required=False, help_text = 'Optional until checkout')
	city = forms.CharField(max_length=255, required=False, help_text = 'Optional until checkout')
	country = forms.CharField(max_length=255, required=False, help_text = 'Optional until checkout')


	class Meta:
		model = User
		fields = ('username', 'firstname', 'lastname', 'password1', 
			'password2', 'email', 'agentid', 'street', 'city', 'country')
	
	# def __init__(self, *args, **kwargs):
	# 	user = kwargs.pop('user', '')
	# 	super(SignUpForm, self).__init__(*args, **kwargs)
	# 	self.fields['assignedagent'] = forms.ModelChoiceField(queryset = assignedagent.objects.filter(owner=user))


	def save(self, commit=True):
		user = User.objects.create_user(username=self.cleaned_data['username'], password=self.cleaned_data['password1'])
		user.email = self.clean_email()
		user.first_name = self.cleaned_data['firstname']
		user.last_name = self.cleaned_data['lastname']
		if commit:
			user.save()
		return user

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Username already in use')

	def clean_email(self):
		email = self.cleaned_data['email']
		if email != '':
			try:
				user = User.objects.get(email=email)
			except User.DoesNotExist:
				return email
			raise forms.ValidationError('Email already in use')

class LoginForm(forms.Form):
	username = forms.CharField(max_length=30, required=True)
	password = forms.CharField(widget=forms.PasswordInput(), max_length=30, required=True)

	# def clean_username(self):
	# 	username = self.cleaned_data['username']
	# 	try:
	# 		user = User.objects.get(username=username)
	# 	except User.DoesNotExist:
	# 		return username
	# 	raise forms.ValidationError('Username already in use')

	# def clean_password(self):
	# 	password = self.cleaned_data['password']
	# 	if password == '':
	# 		raise forms.ValidationError('Field required')
	# 	else:
	# 		return password