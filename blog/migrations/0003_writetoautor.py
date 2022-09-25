# Generated by Django 4.1.1 on 2022-09-24 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_posts_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='WriteToAutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50, verbose_name='Тема')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'сообщение',
                'verbose_name_plural': 'Обратная связь',
                'ordering': ['-id'],
            },
        ),
    ]
