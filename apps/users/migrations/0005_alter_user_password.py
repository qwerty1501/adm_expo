# Generated by Django 3.2.9 on 2023-06-19 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20230617_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$260000$Ps7zUQ1B3pBjAVK4VQ4bS8$QNMG8o/FSGKPvfa8ifEOXhGeQqLmr2QxnEUm2wSRrSo=', max_length=128, verbose_name='Пароль'),
        ),
    ]
