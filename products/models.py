from django.db import models
from django.utils.timezone import now


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_date = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.title
