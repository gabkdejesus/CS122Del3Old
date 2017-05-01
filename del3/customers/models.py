from django.db import models
from django.contrib.auth.models import User

from agents.models import Agent

class Customer(models.Model):
	user_id = models.OneToOneField(User, db_column='customer_id', blank=True, default=1, primary_key=True)
	agent_id = models.ForeignKey(Agent, db_column='agent_id', blank=True, null=True, default=1)
	# first_name = models.CharField(max_length=255, blank=True, null=True)
	# last_name = models.CharField(max_length=255, blank=True, null=True)
	street = models.CharField(max_length=255, blank=True, null=True)
	city = models.CharField(max_length=255, blank=True, null=True)
	country = models.CharField(max_length=255, blank=True, null=True)

	class Meta:
		app_label = 'customers'
		db_table = 'customer'

	def __str__(self):
		return str(self.customer_id)