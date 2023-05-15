# Generated by Django 3.2.9 on 2023-05-12 20:26

import apps.main_page.services
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0007_auto_20230510_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='')),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.main_page.services.get_upload_path, verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'ModelName',
                'verbose_name_plural': 'ModelNames',
                'db_table': 'members',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=256, null=True, verbose_name='Заголовок')),
                ('urel_video', models.URLField(max_length=128, verbose_name='Укажите ссылку на видео')),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
                'db_table': 'video',
            },
        ),
    ]
