from django.db import models
# class Product(models.Model):
# 	product_name = models.CharField('Product Name', max_length=200, default='product name')
# 	product_price = models.DecimalField('Product Pric', decimal_places=2, max_digits=11, default=0.00)
# 	def __str__(self):
# 		return self.product_name()

class Product(models.Model):
	product_no = models.AutoField(primary_key=True)
	product_name = models.CharField(max_length=255, blank=True, null=True)
	color = models.CharField(max_length=255, blank=True, null=True)
	quantity_stocked = models.IntegerField(blank=True, null=True)
	personalization_limit = models.IntegerField(blank=True, null=True)
	price = models.FloatField(blank=True, null=True)

	class Meta:
		app_label = 'catalog'
		db_table = 'product'