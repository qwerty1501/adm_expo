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
    workemail = models.EmailField(verbose_name="Email", default=None, unique=True, **parametersForNull);
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
    ########  Как вы узнали о мероприятие?   #########
    instagram_bool = models.BooleanField(verbose_name="Инстаграм", default=False)
    tv_radio = models.BooleanField(verbose_name="ТВ, Радио", default=False)
    news_portals = models.BooleanField(verbose_name="Новостные порталы", default=False)
    other_two = models.BooleanField(verbose_name="Другое", default=False)
    
    participant_sector = models.CharField(max_length=300, verbose_name="В качестве кого вы хотите посетить HIT EXPO ?", **parametersForNull);
    
    position_main = models.CharField(max_length=300, verbose_name="Должность", **parametersForNull);
    email = models.EmailField(verbose_name="Электронная почта", default=None, unique=True, **parametersForNull);
    password = models.CharField(max_length=128, verbose_name="Пароль", default=make_password(settings.DEFAULT_PASSWORD));

    avatarHidden = models.BooleanField(default=True)
                
    #########################################        СМИ       #########################################
        
    image_certificate_smi = models.ImageField(verbose_name="Загрузите вашего журналистского удостоверения в  png или jpg", upload_to='images/certificate-smi', **parametersForNull);
    image_logo = models.ImageField(verbose_name="Загрузите логотип компании в png или jpg", upload_to='images/logo-smi', **parametersForNull);
    
    organization_smi = models.CharField(max_length=300, verbose_name="Полное юридическое наименование организации", **parametersForNull);
    address = models.CharField(max_length=300, verbose_name="Юридический адрес", **parametersForNull);
    web_site = models.URLField(verbose_name="Веб-сайт", **parametersForNull);
    work_phone = models.CharField(max_length=300, verbose_name="Рабочий телефон", **parametersForNull);
    email_smi = models.EmailField(max_length=300, verbose_name="Email", default=None, unique=True, **parametersForNull);
    
    smi_team = models.CharField(max_length=300, verbose_name="Сколько у вас человек в команде?", **parametersForNull);
    
    
    #############################################       Участник           ##########################################

    participation_sector = models.CharField(max_length=300, verbose_name="Выберите сектор участия (с условиями участия каждого сектора можно ознакомится)", **parametersForNull);
    trade = models.CharField(max_length=300, verbose_name="Выберите отрасль", **parametersForNull);
        
    brand = models.CharField(max_length=300, verbose_name="Наименование бренда", **parametersForNull);
    organization_participant = models.CharField(max_length=300, verbose_name="Полное юридическое наименование организации", **parametersForNull);
    
    inn = models.CharField(max_length=300, verbose_name="ИНН", **parametersForNull);
    p_c = models.CharField(max_length=300, verbose_name="Р/С", **parametersForNull);
    bik = models.CharField(max_length=300, verbose_name="БИК", **parametersForNull);
    okpo = models.CharField(max_length=300, verbose_name="ОКПО", **parametersForNull);
    
    pdf_file = models.FileField(verbose_name="Загрузите свидетельство регистрации в pdf", upload_to='file/register', **parametersForNull)
    name_manager = models.CharField(max_length=300, verbose_name="Ф.И.О руководителя", **parametersForNull);
    position_participant = models.CharField(max_length=300, verbose_name="Должность (Участник)", **parametersForNull);
    company = models.CharField(max_length=300, verbose_name="Деятельность компании", **parametersForNull);
    description = models.TextField(verbose_name="Описание", **parametersForNull);


    email_participant = models.EmailField(max_length=300, verbose_name="Email", default=None, unique=True, **parametersForNull);
    
    
    ###############################################         Контактные лица          #########################################

    name_contact_person = models.CharField(max_length=300, verbose_name="Ф.И.О (контактным лицом)", **parametersForNull);
    position_contact_person = models.CharField(max_length=300, verbose_name="Должность (контактным лицом)", **parametersForNull);
    phone_contact_person = models.CharField(max_length=300, verbose_name="Телефон (контактным лицом)", **parametersForNull);
    whatsapp_contact_person = models.CharField(max_length=300, verbose_name="WhatsApp (контактным лицом)", **parametersForNull);

    # socials
    instagram = models.URLField(verbose_name="Instagram", **parametersForNull);
    facebook = models.URLField(verbose_name="Facebook", **parametersForNull);
    twitter = models.URLField(verbose_name="Twitter", **parametersForNull);
    
    #####################################   Investment    #################################
    
    agricultural_production = models.BooleanField(verbose_name="Производство + сельхоз", default=False)
    construction = models.BooleanField(verbose_name="Строительство", default=False)
    technique = models.BooleanField(verbose_name="Строительство + техника", default=False)
    textiles = models.BooleanField(verbose_name="Текстиль, обувь и аксессуары", default=False)
    education = models.BooleanField(verbose_name="Образование", default=False)
    medicine = models.BooleanField(verbose_name="Медицина", default=False)
    tourism = models.BooleanField(verbose_name="Туризм", default=False)
    echo = models.BooleanField(verbose_name="Эко", default=False)
    it = models.BooleanField(verbose_name="IT", default=False)
    banks = models.BooleanField(verbose_name="Банки", default=False)
    kfx = models.BooleanField(verbose_name="КФХ", default=False)
    krc = models.BooleanField(verbose_name="КРС", default=False)
    machinery = models.BooleanField(verbose_name="Машиностроение", default=False)
    industry = models.BooleanField(verbose_name="Текстильное промышленность", default=False)
    
    
    #####################################################################
    
    choose_direction_fashion = models.CharField(max_length=300, verbose_name="Выберите направление (Fashion)", **parametersForNull);
    choose_direction_food = models.CharField(max_length=300, verbose_name="Выберите направление (Food)", **parametersForNull);
    choose_direction_expert = models.CharField(max_length=300, verbose_name="Эксперт", **parametersForNull);
    
    status = models.CharField(max_length=300, verbose_name="Статус", **parametersForNull);
    manager = models.CharField(max_length=300, verbose_name="Менеджер", **parametersForNull);
    referal = models.CharField(max_length=300, verbose_name="Реферал", **parametersForNull);
    
    ####################################.       PASSWORD    #################################
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