from django.db import models
from products.models import Product
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)
    address = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        total = 0
        for item in self.items.all():
            total += item.price

        return total

    def __str__(self):
        return f'Order {self.id} by {self.user}'
