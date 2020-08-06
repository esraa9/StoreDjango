from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart
from django.contrib.auth.decorators import login_required
from products.models import Product


# Create your views here.
@login_required
def cart(request):
    return render(request, 'carts/cart.html', {'cart': request.user.cart})


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = Cart.objects.get(user=request.user)
    cart.items.add(product)

    return redirect('cart')


@login_required
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = Cart.objects.get(user=request.user)
    cart.items.remove(product)

    return redirect('cart')



def clear_cart(request):
    cart = Cart.objects.get(user=request.user)
    cart.items.clear()

    return redirect('cart')

# @login_required
# def cart(request):
#     user = request.user
#     products = user.cart.items.all()
#     total_price = user.cart.total_price()
#     return render(request, 'carts/cart.html', {'products': products, 'total_price':total_price})
