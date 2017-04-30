from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.admin.views.decorators import staff_member_required

from .models import Product

from .forms import ProductForm

def index(request):
	if request.method == 'POST':
		if request.user.is_staff: 
			form = ProductForm(request.POST)
			if form.is_valid():
				product_name = form.cleaned_data.get('product_name')
				product_price = form.cleaned_data.get('product_price')
				product = Product(product_name=product_name, product_price=product_price)
				product.save()
				return HttpResponseRedirect(reverse('catalog:index'))
		else:
			return HttpResponse('Not allowed to add product')
	product_list = Product.objects.all()
	return render(request, 'catalog/index.html', {'product_list': product_list})

@staff_member_required
def add_product(request):
	if request.user.is_staff:
		return render(request, 'catalog/addproduct.html')
	else:
		return HttpResponseRedirect(reverse('catalog:index'))

@staff_member_required
def delete_product(request, product_id):
	product = Product.objects.get(pk=product_id)
	product.delete()
	return HttpResponseRedirect(reverse('catalog:index'))
