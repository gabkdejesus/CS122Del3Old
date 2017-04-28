from django.db import models

class Product(models.Model):
	product_name = models.CharField('Product Name', max_length=200, default='product name')
	product_price = models.DecimalField('Product Price', decimal_places=2, max_digits=11, default=0.00)
	def __str__(self):
		return self.product_name


