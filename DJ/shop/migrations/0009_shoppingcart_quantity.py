# Generated by Django 4.2.3 on 2023-09-03 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_mobile_description_alter_mobile_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=1, max_length=5),
        ),
    ]