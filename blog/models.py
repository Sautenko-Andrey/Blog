from django.db import models
from django.urls import reverse

class Posts(models.Model):
    title=models.CharField(max_length=255)
    slug=models.SlugField(max_length=255, unique=True, db_index=True,verbose_name='URL')
    content=models.TextField(blank=True)
    photo=models.ImageField(upload_to='photos/%Y/%m/%d/')
    time_create=models.DateTimeField(auto_now_add=True)
    time_update=models.DateTimeField(auto_now=True)
    is_published=models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post',kwargs={'post_slug':self.slug})

    class Meta:
        verbose_name='Посты'
        verbose_name_plural='Посты'
        ordering=['-time_create','title']

class MainPageText(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(blank=True)
    picture_1=models.ImageField(upload_to='photos/%Y/%m/%d/',null=True)
    picture_2 = models.ImageField(upload_to='photos/%Y/%m/%d/',null=True)
    picture_3 = models.ImageField(upload_to='photos/%Y/%m/%d/',null=True)

    class Meta:
        verbose_name='Контент главной страницы'
        verbose_name_plural='Контент главной страницы'

class SocialNet(models.Model):
    instagram=models.CharField(max_length=250)
    facebook=models.CharField(max_length=250)
    youtube=models.CharField(max_length=250)

    class Meta:
        verbose_name='Соцсети'
        verbose_name_plural='Соцсети'


