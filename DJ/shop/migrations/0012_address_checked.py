# Generated by Django 4.2.3 on 2023-09-25 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_alter_shoppingcart_mobile_alter_shoppingcart_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='checked',
            field=models.BooleanField(default=0),
        ),
    ]
