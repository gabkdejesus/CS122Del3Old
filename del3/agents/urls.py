from django.conf.urls import url

from . import views as agents_views

urlpatterns = [
    url(r'^$', agents_views.index, name='index'),
    url(r'^delete/(?P<agent_no>[0-9]+)/$', agents_views.delete_agent, name='delete_agent')
]