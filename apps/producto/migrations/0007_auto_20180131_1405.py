# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-31 22:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0006_producto_cantidad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='cantidad',
            new_name='unidades',
        ),
    ]
