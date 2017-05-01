from django.db import models

class Agent(models.Model):
	agent_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=255, blank=True, null=True)
	last_name = models.CharField(max_length=255, blank=True, null=True)
	total_transactions = models.IntegerField(blank=True, null=True)

	class Meta:
		app_label = 'agents'
		db_table = 'agent'

	def __str__(self):
		return str(self.agent_id)