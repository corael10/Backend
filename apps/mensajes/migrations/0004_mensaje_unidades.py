# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-11 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensajes', '0003_auto_20180607_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje',
            name='unidades',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
