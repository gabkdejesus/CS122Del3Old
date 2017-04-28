from django.shortcuts import render
from django.http import HttpResponse

from .models import Agent

def index(request):
	agent_list = Agent.objects.all()
	return render(request, 'agents/index.html', {'agent_list': agent_list})

