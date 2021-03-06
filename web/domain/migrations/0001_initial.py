# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-01-16 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='\u57df\u540d')),
                ('url', models.CharField(max_length=100, verbose_name='URL\u8fde\u63a5')),
                ('status', models.SmallIntegerField(choices=[(0, '\u4e0d\u56de\u6e90'), (1, '\u56de\u6e90')], default=0, verbose_name='\u662f\u5426\u56de\u6e90')),
                ('proxy', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u56de\u6e90\u5730\u5740')),
                ('add_date', models.DateField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('update_date', models.DateField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
            ],
            options={
                'db_table': 'domain',
                'verbose_name': '\u57df\u540d\u7ba1\u7406',
                'verbose_name_plural': '\u57df\u540d\u7ba1\u7406',
            },
        ),
    ]
