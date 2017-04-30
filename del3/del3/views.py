from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.models import User
from .forms import SignUpForm, LoginForm

def index(request):
	return render(request, 'del3/index.html')

def signup(request):
	if not request.user.is_authenticated():
		if request.method == 'POST':
			form = SignUpForm(request.POST)
			if form.is_valid():
				username = form.clean_username()
				password = form.cleaned_data.get('password1')
				form.save()
				# firstname = form.cleaned_data.get('firstname')
				# lastname = form.cleaned_data.get('lastname')
				# auth_login(request, user)
				# new_user = User.objects.create_user(username=username, password=password, email='', first_name='', last_name='')
				# if email: new_user.email = email
				# if firstname: new_user.first_name = firstname
				# if lastname: new_user.last_name = lastname

				user = authenticate(username=username, password=password)
				auth_login(request, user)
				return HttpResponseRedirect(reverse('catalog:index'))
			else:
				return render(request, 'del3/signup.html', {'form': form})
		else:
			form = SignUpForm()
			return render(request, 'del3/signup.html', {'form': form})
	else:
		return HttpResponseRedirect(reverse('index'))

def login(request):
	if not request.user.is_authenticated():
		if request.method == 'POST':
			form = LoginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				user = authenticate(username=username, password=password)
				if user is not None:
					if user.is_active:
						auth_login(request, user)
						return HttpResponseRedirect(reverse('index'))
					else:
						return HttpResponse('User inactive')
				else:
					return render(request, 'del3/login.html', {'form': form, 'warning': 'Username or password is incorrect.'})
			else:
				return render(request, 'del3/login.html', {'form': form})
		else:
			form = LoginForm()
			return render(request, 'del3/login.html', {'form': form})
	else:
		return HttpResponseRedirect(reverse('index'))

def logout(request):
	auth_logout(request)
	return HttpResponseRedirect(reverse('index'))