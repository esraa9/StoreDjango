from django.urls import path
from .views import add_to_cart, cart, remove_form_cart, remove_all

urlpatterns = [

    path('add/<product_id>', add_to_cart, name='add_to_cart'),
    path('', cart, name='cart'),
    path('remove_form_cart/<product_id>', remove_form_cart, name='remove_form_cart'),
    path('removeall', remove_all, name='remove_all'),

]
