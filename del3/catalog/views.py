from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Product

from .forms import ProductForm

def index(request):
	if request.method == 'POST':
		form = ProductForm(request.POST)
		if form.is_valid():
			product_name = form.cleaned_data.get('product_name')
			product_price = form.cleaned_data.get('product_price')
			product = Product(product_name=product_name, product_price=product_price)
			product.save()
			return HttpResponseRedirect(reverse('catalog:index'))
	product_list = Product.objects.all()
	return render(request, 'catalog/index.html', {'product_list': product_list})

def add_product(request):
	return render(request, 'catalog/addproduct.html')

def delete_product(request, product_id):
	product = Product.objects.get(pk=product_id)
	product.delete()
	return HttpResponseRedirect(reverse('catalog:index'))
