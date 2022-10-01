# Generated by Django 4.1.1 on 2022-09-28 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_aboutsite_facebook_link_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('picture_1', models.ImageField(null=True, upload_to='photos/%Y/%m/%d/')),
                ('picture_2', models.ImageField(null=True, upload_to='photos/%Y/%m/%d/')),
                ('picture_3', models.ImageField(null=True, upload_to='photos/%Y/%m/%d/')),
                ('show_or_hide', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Рассказы о городах',
                'verbose_name_plural': 'Рассказы о городах',
            },
        ),
    ]