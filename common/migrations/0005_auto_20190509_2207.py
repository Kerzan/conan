# Generated by Django 2.1 on 2019-05-09 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_group_is_activate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='source',
            field=models.CharField(blank=True, max_length=254, verbose_name='来源'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='tip',
            field=models.TextField(blank=True, verbose_name='提示'),
        ),
    ]
