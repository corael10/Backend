# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-30 00:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='precio',
        ),
        migrations.DeleteModel(
            name='Precio',
        ),
    ]