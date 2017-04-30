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

	def save(self, commit=True):
		user = super(SignUpForm, self).save(commit=False)
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