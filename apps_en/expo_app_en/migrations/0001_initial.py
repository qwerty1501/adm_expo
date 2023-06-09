# Generated by Django 3.2.9 on 2023-06-17 11:38

import apps_en.expo_app_en.services
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelEn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
                ('image', models.ImageField(upload_to='', verbose_name='Фотография')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('ulr', models.URLField(blank=True, null=True, verbose_name='Укажите *url сайта')),
                ('location', models.URLField(blank=True, null=True, verbose_name='Укажите *url локации')),
            ],
            options={
                'verbose_name': 'Гостиница',
                'verbose_name_plural': 'Гостиница',
                'db_table': 'hotel_en',
            },
        ),
        migrations.CreateModel(
            name='StandEn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[['GENERAL', 'GENERAL'], ['PLATINUM+', 'PLATINUM+'], ['PLATINUM', 'PLATINUM'], ['Gold+', 'Gold+'], ['Gold', 'Gold'], ['SILVER+', 'SILVER+'], ['SILVER', 'SILVER'], ['STANDARD+', 'STANDARD+'], ['STANDARD', 'STANDARD']], default=None, max_length=32, verbose_name='Тип стендов')),
                ('square', models.CharField(blank=True, max_length=16, null=True, verbose_name='Площадь')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.CharField(blank=True, max_length=16, null=True, verbose_name='')),
            ],
            options={
                'verbose_name': 'ОПЦИИ ВЫСТАВОЧНЫХ СТЕНДОВ',
                'verbose_name_plural': 'ОПЦИИ ВЫСТАВОЧНЫХ СТЕНДОВ',
                'db_table': 'stand_en',
            },
        ),
        migrations.CreateModel(
            name='LocationEn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=32, verbose_name='Адресс')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('location', models.CharField(blank=True, max_length=256, null=True, verbose_name='Ссылка для локации')),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps_en.expo_app_en.services.get_upload_path, validators=[apps_en.expo_app_en.services.validate_file_extension], verbose_name='Фотография')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'location',
                'verbose_name_plural': 'locations',
                'db_table': 'locations_en',
            },
        ),
    ]
