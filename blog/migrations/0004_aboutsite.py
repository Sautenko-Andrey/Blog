# Generated by Django 4.1.1 on 2022-09-26 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_writetoautor'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'О сайте',
                'verbose_name_plural': 'О сайте',
            },
        ),
    ]
