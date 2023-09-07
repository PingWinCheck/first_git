# Generated by Django 4.2.3 on 2023-09-03 18:48

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0009_shoppingcart_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingcart',
            name='mobile',
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='mobile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.mobile'),
        ),
    ]