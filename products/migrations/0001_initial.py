# Generated by Django 4.2.6 on 2023-10-12 11:00

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('country', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('category', models.CharField(choices=[('meat', 'Meat'), ('fruit', 'Fruit'), ('vegetables', 'Vegetables'), ('wine', 'Wine'), ('beer', 'Beer'), ('honey', 'Honey'), ('nuts', 'Nuts'), ('cheese', 'Cheese'), ('mix', 'Mix of products'), ('other', 'Other')], default='other', max_length=50)),
                ('price', models.FloatField()),
                ('available', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated_date'],
            },
        ),
    ]
