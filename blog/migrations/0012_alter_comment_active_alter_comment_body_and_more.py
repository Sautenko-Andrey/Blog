# Generated by Django 4.1.1 on 2022-10-04 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_comment_options_alter_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Видимость комментария'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(max_length=255, verbose_name='Текст комментария'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Автор комментария'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_posts', to='blog.posts', verbose_name='Статья'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения'),
        ),
    ]
