"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from products.views import products_list, product_details, product_add, product_edit, product_delete
from django.conf import settings
from django.conf.urls.static import static


def home(request):
    return redirect('products_list')


urlpatterns = [
      path('admin/', admin.site.urls),
      path('', home, name='home'),
      path('products/', products_list, name='products_list'),
      path('products/add', product_add, name='products_add'),
      path('products/delete/<pk>', product_delete, name='product_delete'),
      path('products/<pk>', product_details, name='product_details'),
      path('products/edit/<pk>', product_edit, name='product_edit'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
