# Generated by Django 3.2.9 on 2023-06-19 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='facebook',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Укажите url Facebook'),
        ),
        migrations.AlterField(
            model_name='user',
            name='instagram',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Укажите url Instagram'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$260000$JD5vPQQRxINiJUVf8csIPQ$Z+0hqSrmMVtsCTMWoAWNQzzN0xgkBqBYjA18drgQwpI=', max_length=128, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='user',
            name='twitter',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Укажите url Twitter'),
        ),
        migrations.AlterField(
            model_name='user',
            name='web_site',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Укажите url Веб-сайта'),
        ),
    ]
