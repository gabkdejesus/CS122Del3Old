from django import forms

class ProductForm(forms.Form):
	product_name = forms.CharField(max_length=250, required=True)
	product_price = forms.DecimalField(decimal_places=2, max_digits=11, required=True)
