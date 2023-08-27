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



class Firm(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Фирма')

    class Meta:
        verbose_name = 'Фирма'
        verbose_name_plural = 'Фирмы'

    def __str__(self):
        return self.name
