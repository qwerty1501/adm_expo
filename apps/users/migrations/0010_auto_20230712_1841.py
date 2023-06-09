# Generated by Django 3.2.9 on 2023-07-12 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20230712_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='quantity_person_smi',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Сколько у вас человек в команде ?'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$260000$s5cepPVMkNn0nj1C0iTkW0$ItgA9TZM+eBX7choLCnAUuDsPzL7+0NXXLlEkW52cQo=', max_length=128, verbose_name='Пароль'),
        ),
    ]
