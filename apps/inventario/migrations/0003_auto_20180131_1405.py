# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-31 22:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_auto_20180131_1113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productos_inventario_entrada',
            old_name='cantidad',
            new_name='unidades',
        ),
    ]
