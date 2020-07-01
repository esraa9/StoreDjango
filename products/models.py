from django.db import models


# Create your models here.
class product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300, blank=True, null=True)


    def __str__(self):
        return self.title +" " + self.description

