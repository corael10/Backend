# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-09 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0008_auto_20180209_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos_inventario_entrada',
            name='folio',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]