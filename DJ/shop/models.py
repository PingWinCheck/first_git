from django.db import models

# Create your models here.
class Mobile(models.Model):
    firm = models.ForeignKey('Firm', on_delete=models.PROTECT, null=True, verbose_name='Фирма')
    name = models.CharField(max_length=100, verbose_name='Модель')
    description = models.CharField(max_length=255, verbose_name='Описание')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    photo = models.ImageField(verbose_name='Фото')
    quantity = models.IntegerField(verbose_name='Кол-во')
    slug = models.SlugField(max_length=255)


    class Meta:
        verbose_name = 'Мобильный телефон'
        verbose_name_plural = 'Мобильные телефоны'



    def __str__(self):
        return self.name

class Firm(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Фирма')

    class Meta:
        verbose_name = 'Фирма'
        verbose_name_plural = 'Фирмы'

    def __str__(self):
        return self.name
