from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models

# Create your models here.
from django.urls import reverse


class Mobile(models.Model):
    firm = models.ForeignKey('Firm', on_delete=models.PROTECT, null=True, verbose_name='Фирма')
    name = models.CharField(max_length=100, verbose_name='Модель')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    photo = models.ImageField(verbose_name='Фото')
    quantity = models.PositiveSmallIntegerField(verbose_name='Кол-во', default=0)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Мобильный телефон'
        verbose_name_plural = 'Мобильные телефоны'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('info_mobile', kwargs={'slug': self.slug})


class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    mobile = models.ForeignKey(Mobile, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(5)])
    status = models.ForeignKey('OrderStatus', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.user.username + self.mobile.name


class OrderStatus(models.Model):
    status = models.CharField(max_length=25)

    def __str__(self):
        return self.status


class Firm(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Фирма')

    class Meta:
        verbose_name = 'Фирма'
        verbose_name_plural = 'Фирмы'

    def __str__(self):
        return self.name


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    home = models.CharField(max_length=15)
    flat = models.PositiveSmallIntegerField(blank=True, null=True)
    checked = models.BooleanField(default=0)

    def __str__(self):
        if self.flat:
            return f'{self.user}  |  {self.city}, {self.street}, {self.home}, {self.flat}'
        return f'{self.user}  |  {self.city}, {self.street}, {self.home}'
