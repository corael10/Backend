# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-20 00:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0009_familia_marca'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio_promo',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
