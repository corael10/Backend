# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-08 00:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0005_inventario_entrada_fecha_proveedor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productos_inventario_entrada',
            old_name='Inventario_entrada',
            new_name='inventario_entrada',
        ),
    ]
