from django.urls import path
from .views import order, order_list


urlpatterns = [

    path('orders/', order_list, name='order_list'                                    ''),
    path('orders/add/', order, name='order'),

]
