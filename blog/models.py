from django.db import models
from django.urls import reverse


class Posts(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Посты'
        verbose_name_plural = 'Посты'
        ordering = ['-time_create', 'title']


class AboutSite(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    my_phone=models.CharField(blank=True,max_length=13)
    my_mail=models.CharField(blank=True,max_length=30)
    facebook_link=models.CharField(blank=True,max_length=100)
    instagram_link=models.CharField(blank=True,max_length=100)
    youtube_link=models.CharField(blank=True,max_length=100)
    linkedn_link=models.CharField(blank=True,max_length=100)

    class Meta:
        verbose_name = 'Контент страницы <О блоге>'
        verbose_name_plural = 'Контент страницы <О блоге>'


class MainPageText(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    picture_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True)
    picture_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True)
    picture_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True)

    class Meta:
        verbose_name = 'Контент главной страницы'
        verbose_name_plural = 'Контент главной страницы'


class SocialNet(models.Model):
    instagram = models.CharField(max_length=250)
    facebook = models.CharField(max_length=250)
    youtube = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Соцсети'
        verbose_name_plural = 'Соцсети'


class WriteToAutor(models.Model):
    title = models.CharField(blank=False, max_length=50, db_index=True, verbose_name='Тема')
    message = models.TextField(blank=False, verbose_name='Сообщение')
    email = models.CharField(blank=False, max_length=50, verbose_name='Email')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'Обратная связь'
        ordering = ['-id']


class City(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(blank=False)
    content_2part = models.TextField(blank=False,null=True)
    picture_1=models.ImageField(upload_to='photos/%Y/%m/%d/', null=True)
    picture_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True)
    picture_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True)
    show_or_hide = models.BooleanField(default=True)

    class Meta:
        verbose_name='Рассказы о городах'
        verbose_name_plural='Рассказы о городах'

class Sponsorship(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField(max_length=255)
    card_1=models.CharField(max_length=16)
    card_2 = models.CharField(max_length=16)
    card_3 = models.CharField(max_length=16)

    class Meta:
        verbose_name='Спонсорство'
        verbose_name_plural='Спонсорство'