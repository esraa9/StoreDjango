from django.urls import path
from products.views import products_list, product_details, product_add, product_edit, product_delete

urlpatterns = [

    path('products/', products_list, name='products_list'),
    path('products/add', product_add, name='products_add'),
    path('products/delete/<pk>', product_delete, name='product_delete'),
    path('products/<pk>', product_details, name='product_details'),
    path('products/edit/<pk>', product_edit, name='product_edit'),

]
