from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.admin.views.decorators import staff_member_required

from .models import Agent

def index(request):
	agent_list = Agent.objects.all()
	attribs = Agent._meta.fields
	return render(request, 'agents/index.html', {'agent_list': agent_list, 'attribs': attribs})

@staff_member_required
def delete_agent(request, agent_no):
	agent = Agent.objects.get(pk=agent_no)
	agent.delete()
	return HttpResponseRedirect(reverse('agent:index'))