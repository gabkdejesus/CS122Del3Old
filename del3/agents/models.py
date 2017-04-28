from django.db import models

class Agent(models.Model):
	agent_first_name = models.CharField('First Name', max_length=200, default='John')
	agent_last_name = models.CharField('Last Name', max_length=200, default='Smith')
	def __str__(self):
		return self.agent_last_name + self.agent_last_name