# Generated by Django 3.2.9 on 2023-05-22 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_organic', models.CharField(max_length=128, verbose_name='Название организации')),
                ('surname', models.CharField(max_length=16, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=16, verbose_name='Имя')),
                ('email', models.EmailField(max_length=32, verbose_name='E-mail')),
                ('number', models.CharField(max_length=16, verbose_name='Телефон')),
                ('user_status', models.CharField(blank=True, choices=[['Партнер', 'Партнер'], ['Участник', 'Участник']], default=None, max_length=100, null=True, verbose_name='Выберите направление')),
            ],
            options={
                'verbose_name': 'ПРЕДВАРИТЕЛЬНАЯ ЗАЯВКА',
                'verbose_name_plural': 'ПРЕДВАРИТЕЛЬНАЯ ЗАЯВКА',
                'db_table': 'application_en',
            },
        ),
    ]
