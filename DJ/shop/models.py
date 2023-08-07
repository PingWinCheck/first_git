from django.db import models

# Create your models here.
class Mobile(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    slug = models.SlugField(max_length=255, null=True)
    def __str__(self):
        return f'{self.name} - {self.price}'
