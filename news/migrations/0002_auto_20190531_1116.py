# Generated by Django 2.0.6 on 2019-05-31 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Фото', 'verbose_name_plural': 'Фотографії'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новина', 'verbose_name_plural': 'Новини'},
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата'),
        ),
    ]