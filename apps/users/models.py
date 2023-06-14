import uuid
import os

from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from apps.users.managers import CustomManager
from django.db import models


parametersForNull = {
    'null': True,
    'blank': True,
}


class Rename:
    def __init__(self, path):
        self.path = path;
        
    def rename(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = '%s.%s' % (uuid.uuid4(), ext)
        return os.path.join(self.path, filename)



class User(AbstractUser):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи";

    def __str__(self):
        return self.uniqueId.__str__();

    username = None;
    date_joined = None;
    first_name = None;
    last_name = None;
    last_login = None;
    is_active = models.BooleanField(default=True, verbose_name="Активный?");
    is_staff = models.BooleanField(default=False, verbose_name="Админ?");
    is_superuser = models.BooleanField(default=False, verbose_name="СуперАдмин?");

    name = models.CharField(max_length=300, verbose_name="Ф.И.О", **parametersForNull);
    workEmail = models.EmailField(verbose_name="Email", default=None, unique=True, **parametersForNull);
    country = models.CharField(max_length=300, verbose_name="Страна", **parametersForNull);
    city = models.CharField(max_length=300, verbose_name="Город", **parametersForNull);
    birth = models.CharField(max_length=300, verbose_name="Дата рождения", **parametersForNull);
    
    image_id_one = models.ImageField(verbose_name="Аватар", upload_to='images/passport_one', **parametersForNull);
    image_id_two = models.ImageField(verbose_name="Аватар", upload_to='images/passport_two', **parametersForNull);
    image_id_three = models.ImageField(verbose_name="Аватар", upload_to='images/passport_three', **parametersForNull);
    
    workPhone = models.CharField(max_length=300, verbose_name="Телефон", **parametersForNull);
    personalPhone = models.CharField(max_length=300, verbose_name="WhatsApp", **parametersForNull);
    ####### Я заинтересован в #########
    visit = models.BooleanField(verbose_name="Посещение на HIT EXPO", default=False)
    participation = models.BooleanField(verbose_name="Участие на HIT EXPO", default=False)
    projects = models.BooleanField(verbose_name="Поиске проектов", default=False)
    other_one = models.BooleanField(verbose_name="Другое", default=False)
    ########  Как вы узнали о мероприятие?   ########
    instagram = models.BooleanField(verbose_name="Инстаграм", default=False)
    tv_radio = models.BooleanField(verbose_name="ТВ, Радио", default=False)
    news_portals = models.BooleanField(verbose_name="Новостные порталы", default=False)
    other_two = models.BooleanField(verbose_name="Другое", default=False)
    
    mass_media = models.ForeignKey("MassMedia", verbose_name="СМИ", on_delete=models.CASCADE, **parametersForNull)
    participant = models.ForeignKey("Participant", verbose_name="СМИ", on_delete=models.CASCADE, **parametersForNull)
    
    position = models.CharField(max_length=300, verbose_name="Должность", **parametersForNull);
    email = models.EmailField(verbose_name="Электронная почта", default=None, unique=True, **parametersForNull);
    password = models.CharField(max_length=128, verbose_name="Пароль", default=make_password(settings.DEFAULT_PASSWORD));

    avatarHidden = models.BooleanField(default=True)
    # bg = models.ImageField(verbose_name="Задний фон", upload_to=bgRename.rename, **parametersForNull);

    uniqueId = models.UUIDField(unique=True, verbose_name="Уникальный id", **parametersForNull);

    resetPasswordUUID = models.UUIDField(verbose_name="Ссылка для восстановления пароля", **parametersForNull);
    resetPasswordDate = models.BigIntegerField(verbose_name="Время восстановления пароля", **parametersForNull);

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = CustomManager()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id:
            self.uniqueId = uuid.uuid4()
        super(User, self).save(force_insert=False, force_update=False, using=None, update_fields=None)
        
        
class MassMedia(models.Model):
    
    class Meta:
        db_table = 'mass_media'
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'
        
    image_certificate_smi = models.ImageField(verbose_name="Загрузите вашего журналистского удостоверения в  png или jpg", upload_to='images/certificate-smi', **parametersForNull);
    image_logo_smi = models.ImageField(verbose_name="Загрузите логотип компании в png или jpg", upload_to='images/logo-smi', **parametersForNull);
    organization_smi = models.CharField(max_length=300, verbose_name="Полное юридическое наименование организации", **parametersForNull);
    address_smi = models.CharField(max_length=300, verbose_name="Юридический адрес", **parametersForNull);
    web_site = models.URLField(verbose_name="Веб-сайт", **parametersForNull);
    work_phone_smi = models.CharField(max_length=300, verbose_name="Рабочий телефон", **parametersForNull);
    email_smi = models.EmailField(max_length=300, verbose_name="Email", default=None, unique=True, **parametersForNull);
    # socials
    instagram = models.URLField(verbose_name="Instagram", **parametersForNull);
    facebook = models.URLField(verbose_name="Facebook", **parametersForNull);
    twitter = models.URLField(verbose_name="Twitter", **parametersForNull);
    
    smi_team = models.CharField(max_length=300, verbose_name="Сколько у вас человек в команде?", **parametersForNull);
    
    def __str__(self):
        return self.name
        # return f'{self.name}'
    

class Participant(models.Model):
    
    class Meta:
        db_table = 'participant'
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'
        
    participation_sector = models.ForeignKey("ParticipationSector", verbose_name='Выберите сектор участия (с условиями участия каждого сектора можно ознакомится)', on_delete=models.CASCADE, **parametersForNull)
    industry = models.ForeignKey("Industry", verbose_name='Выберите отрасль', on_delete=models.CASCADE, **parametersForNull)
    brand = models.CharField(max_length=300, verbose_name="Наименование бренда", **parametersForNull);
    image_logo_participant = models.ImageField(verbose_name="Загрузите логотип компании в png или jpg", upload_to='images/participant', **parametersForNull);
    organization_participant = models.CharField(max_length=300, verbose_name="Полное юридическое наименование организации", **parametersForNull);
    address_participant = models.CharField(max_length=300, verbose_name="Юридический адрес", **parametersForNull);
    
    inn = models.CharField(max_length=300, verbose_name="ИНН", **parametersForNull);
    p_c = models.CharField(max_length=300, verbose_name="Р/С", **parametersForNull);
    bik = models.CharField(max_length=300, verbose_name="БИК", **parametersForNull);
    okpo = models.CharField(max_length=300, verbose_name="ОКПО", **parametersForNull);
    
    pdf_file = models.FileField(verbose_name="Загрузите свидетельство регистрации в pdf", upload_to='file/register', **parametersForNull)
    name = models.CharField(max_length=300, verbose_name="Ф.И.О руководителя", **parametersForNull);
    position = models.CharField(max_length=300, verbose_name="Должность", **parametersForNull);
    company = models.CharField(max_length=300, verbose_name="Деятельность компании", **parametersForNull);
    description = models.TextField(verbose_name="Описание", **parametersForNull);
    web_site = models.URLField(verbose_name="Веб-сайт", **parametersForNull);
    work_phone_smi = models.CharField(max_length=300, verbose_name="Рабочий телефон", **parametersForNull);
    email_participant = models.EmailField(max_length=300, verbose_name="Email", default=None, unique=True, **parametersForNull);
    # socials
    instagram = models.URLField(verbose_name="Instagram", **parametersForNull);
    facebook = models.URLField(verbose_name="Facebook", **parametersForNull);
    twitter = models.URLField(verbose_name="Twitter", **parametersForNull);
    
    dop_participant = models.ForeignKey("DopParticipant", verbose_name='Выберите отрасль', on_delete=models.CASCADE, **parametersForNull)
    
    
class ParticipationSector(models.Model):
    
    class Meta:
        db_table = 'participation_sector'
        verbose_name = 'Выберите сектор участия'
        verbose_name_plural = 'Выберите сектор участии'
        
    name = models.CharField(max_length=300, verbose_name="Наименование сектора");
    
    def __str__(self):
        return self.name
    
    
class Industry(models.Model):
    
    class Meta:
        db_table = 'industry'
        verbose_name = 'Отрасль'
        verbose_name_plural = 'Отрасль'
        
    name = models.CharField(max_length=300, verbose_name="Наименование отраслей");
    
    def __str__(self):
        return self.name
    
    
class DopParticipant(models.Model):
    
    class Meta:
        db_table = 'dop_participant'
        verbose_name = 'Контактные лица'
        verbose_name_plural = 'Контактные лица'
        
    name = models.CharField(max_length=300, verbose_name="Ф.И.О", **parametersForNull);
    position = models.CharField(max_length=300, verbose_name="Должность", **parametersForNull);
    phone = models.CharField(max_length=300, verbose_name="Телефон", **parametersForNull);
    whatsapp_phone = models.CharField(max_length=300, verbose_name="WhatsApp", **parametersForNull);
    
    def __str__(self):
        return self.name