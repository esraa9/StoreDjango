from django.shortcuts import render
from django.http import HttpResponse
from .models import product

# Create your views here.
def products_list(request):
    products = product.objects.all()
    return render(request ,'products-list.html',{'products': products})

