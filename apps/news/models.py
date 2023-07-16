from django.db import models


class News(models.Model):

    class Meta:
        db_table = 'news'
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

    image = models.ImageField(verbose_name="Фотография", upload_to="apps/news/images", blank=True, null=True)
    title = models.CharField(verbose_name="Заголовок", max_length=300)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    urls = models.URLField(verbose_name="Укажите urel ссылку", blank=True, null=True)
    data = models.DateField(verbose_name="Укажите дату", blank=True, null=True)
    
    def __str__(self):
        return self.title
    