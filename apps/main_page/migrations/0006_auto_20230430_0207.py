# Generated by Django 3.2.9 on 2023-04-29 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0005_alter_tasks_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'managed': True, 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='ellipse',
            options={'verbose_name': 'Эллипс', 'verbose_name_plural': 'Эллипс'},
        ),
        migrations.AlterModelOptions(
            name='socials',
            options={'verbose_name': 'Социальный сеть', 'verbose_name_plural': 'Социальные сети'},
        ),
        migrations.AlterModelOptions(
            name='speakers',
            options={'verbose_name': 'Спикер', 'verbose_name_plural': 'Спикеры'},
        ),
        migrations.AlterField(
            model_name='tasks',
            name='number',
            field=models.CharField(max_length=16, verbose_name='Номер задач'),
        ),
    ]
