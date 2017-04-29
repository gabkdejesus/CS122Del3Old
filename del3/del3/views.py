from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from .forms import SignUpForm, LoginForm

def index(request):
	return render(request, 'del3/index.html')

def signup(request):
	if not request.user.is_authenticated():
		if request.method == 'POST':
			form = SignUpForm(request.POST)
			if form.is_valid():
				form.save()
				username = form.cleaned_data.get('username')
				password = form.cleaned_data.get('password1')
				user = authenticate(username=username, password=password)
				auth_login(request, user)
				return HttpResponseRedirect(reverse('catalog:index'))
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
				username = form.cleaned_data.get('username')
				password = form.cleaned_data.get('password')
				user = authenticate(username=username, password=password)
				if user is not None:
					if user.is_active:
						auth_login(request, user)
						return HttpResponseRedirect(reverse('index'))
					else:
						return HttpResponse('User inactive')
				else:
					return HttpResponseRedirect(reverse('signup'))
		return render(request, 'del3/login.html')
	else:
		return HttpResponseRedirect(reverse('index'))

def logout(request):
	auth_logout(request)
	return HttpResponseRedirect(reverse('index'))