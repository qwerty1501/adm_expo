# Generated by Django 3.2.9 on 2023-07-13 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20230713_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gos_bool_four',
            field=models.BooleanField(default=False, verbose_name='Инвестиционные проекты'),
        ),
        migrations.AddField(
            model_name='user',
            name='gos_bool_one',
            field=models.BooleanField(default=False, verbose_name='Присутствие инвесторов'),
        ),
        migrations.AddField(
            model_name='user',
            name='gos_bool_three',
            field=models.BooleanField(default=False, verbose_name='Развитие экономики Кыргызстана'),
        ),
        migrations.AddField(
            model_name='user',
            name='gos_bool_two',
            field=models.BooleanField(default=False, verbose_name='Потенциал выставки'),
        ),
        migrations.AddField(
            model_name='user',
            name='smi_bool_four',
            field=models.BooleanField(default=False, verbose_name='Участие на пресс-конференции'),
        ),
        migrations.AddField(
            model_name='user',
            name='smi_bool_one',
            field=models.BooleanField(default=False, verbose_name='Стать частью информационной поддержки'),
        ),
        migrations.AddField(
            model_name='user',
            name='smi_bool_three',
            field=models.BooleanField(default=False, verbose_name='Освещение и полезная информация'),
        ),
        migrations.AddField(
            model_name='user',
            name='smi_bool_two',
            field=models.BooleanField(default=False, verbose_name='Знакомство с новыми компаниями'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$260000$sI2H9YvCZCZebMZeQsTSrK$v9sN2nTfJ7Vg2QUpcPS0paLoh2DzxaLZ65LvP2rfg3g=', max_length=128, verbose_name='Пароль'),
        ),
    ]
