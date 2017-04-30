from django.db import models

# class Agent(models.Model):
# 	agent_first_name = models.CharField('First Name', max_length=200, default='John')
# 	agent_last_name = models.CharField('Last Name', max_length=200, default='Smith')
# 	def __str__(self):
# 		return self.agent_last_name + self.agent_last_name
class Agent(models.Model):
	agent_no = models.AutoField(primary_key=True)
	agent_first_name = models.CharField(max_length=255, blank=True, null=True)
	agent_last_name = models.CharField(max_length=255, blank=True, null=True)
	total_transactions = models.IntegerField(blank=True, null=True)
	# customer_no = models.ForeignKey('Customer', db_column='customer_no', blank=True, null=True)

	class Meta:
		app_label = 'agents'
		db_table = 'agent'
