# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-09 20:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0011_familia_promoactiva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familia',
            name='marca',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='familia_requests_created', to='producto.Marca'),
        ),
        migrations.AlterField(
            model_name='marca',
            name='proveedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='marca_requests_created', to='proveedor.Proveedor'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='familia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='producto_requests_created', to='producto.Familia'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='marca',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='producto_requests_created', to='producto.Marca'),
        ),
    ]