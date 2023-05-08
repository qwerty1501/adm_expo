from django.db import models
from location_field.models.plain import PlainLocationField

from apps.main_page.services import get_upload_path, validate_file_extension


class Category(models.Model):
    
    class Meta:
        db_table = 'category'
        managed = True
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    parent = models.ForeignKey('self', on_delete=models.PROTECT, related_name='children', blank=True, null=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=get_upload_path, null=True, blank=True)
    icon = models.FileField(upload_to=get_upload_path, validators=[validate_file_extension], null=True, blank=True)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'
    
    
class PageOne(models.Model):
    
    class Meta:
        db_table = 'page_one'
        verbose_name = 'Начало'
        verbose_name_plural = 'Начало'
        
    image = models.ImageField(verbose_name='Фотография', upload_to=get_upload_path, null=True, blank=True)
    year = models.CharField(verbose_name='Год', max_length=8, blank=True, null=True)
    title = models.CharField(verbose_name='Заголовок Экспо', max_length=32, blank=True, null=True)
    description = models.TextField(verbose_name='Описание Экспо')
    
    def __str__(self):
        return self.title
    

class Forum(models.Model):
    
    class Meta:
        db_table = 'forum'
        verbose_name = 'О форуме'
        verbose_name_plural = 'О форуме'
        
    title = models.CharField(verbose_name='Заголовок форма', max_length=32, blank=True, null=True)
    description = models.TextField(verbose_name='Описание форма')
    
    def __str__(self):
        return self.title
    
    
class Target(models.Model):
    
    class Meta:
        db_table = 'target'
        verbose_name = 'Цель'
        verbose_name_plural = 'Цели'
        
    title = models.CharField(verbose_name='Заголовок цели', max_length=32, blank=True, null=True)
    description = models.TextField(verbose_name='Описание цели')
    
    def __str__(self):
        return self.title
    
    
class Tasks(models.Model):
    
    class Meta:
        db_table = 'tasks'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
    
    number = models.CharField(verbose_name='Номер задач', max_length=16)
    description = models.TextField(verbose_name='Описание задач')
    
    def __str__(self):
        return self.number


class Ellipse(models.Model):
    
    class Meta:
        db_table = 'ellipse'
        verbose_name = 'Эллипс'
        verbose_name_plural = 'Эллипс'
        
    company = models.CharField(verbose_name='Компаний', max_length=16, blank=True, null=True)
    countries = models.CharField(verbose_name='Стран', max_length=16, blank=True, null=True)
    meetings = models.CharField(verbose_name='B2B встречи', max_length=16, blank=True, null=True)
    exhibitors = models.CharField(verbose_name='Экспонентов', max_length=16, blank=True, null=True)
    
    
class Sectors(models.Model):
    
    class Meta:
        db_table = 'sectors'
        verbose_name = 'Секторы'
        verbose_name_plural = 'Секторы'
        
    image = models.ImageField(verbose_name='Фотография', upload_to=get_upload_path, null=True, blank=True)
    icon = models.ImageField(verbose_name='Фотография', upload_to=get_upload_path, validators=[validate_file_extension], null=True, blank=True)
    title = models.CharField(verbose_name="Заголовок сектора", max_length=128, blank=True, null=True)
    description = models.TextField(verbose_name='Описание сектора')
    
    def __str__(self):
        return self.title
    

class Place(models.Model):
    
    class Meta:
        db_table = 'location'
        verbose_name = 'Локации'
        verbose_name_plural = 'Локации'
    
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    
    def __str__(self):
        return self.city
    
    
class Speakers(models.Model):
    
    class Meta:
        db_table = 'speakers'
        verbose_name = 'Спикер'
        verbose_name_plural = 'Спикеры'
        
    image = models.ImageField(verbose_name='Фотография', upload_to=get_upload_path, null=True, blank=True)
    name = models.CharField(verbose_name="Полное имя", max_length=32)
    description = models.TextField(verbose_name='Описание')
    
    def __str__(self):
        return self.name
    

class Organizers(models.Model):
    
    class Meta:
        db_table = 'organizers'
        verbose_name = 'Организатор'
        verbose_name_plural = 'Организаторы'
    
    name = models.CharField(verbose_name="Название организации", max_length=32)
    loga = models.ImageField(verbose_name="Фотография нашего организаторa *(157x127)", upload_to=get_upload_path, validators=[validate_file_extension], null=True, blank=True)

    def __str__(self):
        return self.name
    
    
class Sponsors(models.Model):
    
    class Meta:
        db_table = 'sponsors'
        verbose_name = 'Спонсор'
        verbose_name_plural = 'Спонсоры'

    name =models.CharField(verbose_name='Название спонсара', max_length=32)
    loga = models.ImageField(verbose_name="Фотография нашего спонсара *(157x127)", upload_to=get_upload_path, validators=[validate_file_extension], null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    
class Partners(models.Model):
    
    class Meta:
        db_table = 'partners'
        verbose_name = 'Партнёр'
        verbose_name_plural = 'Партёры'

    name =models.CharField(verbose_name='Название партнёра', max_length=32)
    loga = models.ImageField(verbose_name="Логотип нашего партнёра *(157x127)", upload_to=get_upload_path, validators=[validate_file_extension], null=True, blank=True)
    
    def __str__(self):
        return self.name
    

class Socials(models.Model):
    
    class Meta:
        db_table = 'socials'
        verbose_name = 'Социальный сеть'
        verbose_name_plural = 'Социальные сети'
        
    whatsapp = models.URLField(verbose_name="Whatsapp", blank=True, null=True);
    instagram = models.URLField(verbose_name="Instagram", blank=True, null=True);
    facebook = models.URLField(verbose_name="Facebook", blank=True, null=True);
    telegram = models.URLField(verbose_name="Telegram", blank=True, null=True);
    snapchat = models.URLField(verbose_name="Snapchat", blank=True, null=True);
    tiktok = models.URLField(verbose_name="Tiktok", blank=True, null=True);
    twitter = models.URLField(verbose_name="Twitter", blank=True, null=True);
    youtube = models.URLField(verbose_name="Youtube", blank=True, null=True);
    wechat = models.URLField(verbose_name="Wechat", blank=True, null=True);