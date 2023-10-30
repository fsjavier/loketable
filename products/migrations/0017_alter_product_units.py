# Generated by Django 4.2.6 on 2023-10-30 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_product_units'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='units',
            field=models.CharField(choices=[('kg', 'Kg.'), ('gr', 'gr.'), ('liters', 'l.'), ('ml', 'ml.'), ('bottle', 'bottle'), ('bottles', 'bottles'), ('unit', 'unit'), ('units', 'units')], default='unit', max_length=10),
        ),
    ]