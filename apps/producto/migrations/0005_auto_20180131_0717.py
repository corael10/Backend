# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-31 15:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0004_producto_precio_proveedor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='precio_Proveedor',
            new_name='precio_proveedor',
        ),
    ]
