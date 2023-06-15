# Generated by Django 3.2.9 on 2023-06-15 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20230615_1232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='address_participant',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='address_smi',
        ),
        migrations.RemoveField(
            model_name='user',
            name='position',
        ),
        migrations.AddField(
            model_name='user',
            name='manager',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Менеджер'),
        ),
        migrations.AddField(
            model_name='user',
            name='position_participant',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Должность (Участник)'),
        ),
        migrations.AddField(
            model_name='user',
            name='referal',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Реферал'),
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name_contact_person',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Ф.И.О (контактным лицом)'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$260000$o7HAOpuyHoWzPhcnTArCwy$JR5Lna44ot7bwPSm2vyFR5hglQKD6scWNJtLHKg2s7Y=', max_length=128, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_contact_person',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Телефон (контактным лицом)'),
        ),
        migrations.AlterField(
            model_name='user',
            name='position_contact_person',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Должность (контактным лицом)'),
        ),
        migrations.AlterField(
            model_name='user',
            name='whatsapp_contact_person',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='WhatsApp (контактным лицом)'),
        ),
    ]
