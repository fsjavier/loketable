# Generated by Django 4.2.6 on 2023-10-30 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_alter_product_city_alter_product_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='units',
            field=models.CharField(choices=[('kg', 'Kg.'), ('gr', 'gr.'), ('liters', 'l.'), ('ml', 'ml'), ('unit', 'unit'), ('units', 'units')], default='unit', max_length=10),
        ),
    ]
