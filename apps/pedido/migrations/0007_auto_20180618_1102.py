# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-18 18:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0002_auto_20180129_1616'),
        ('pedido', '0006_auto_20180618_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido_entrada',
            name='empleadosustituto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='empleado.Empleado'),
        ),
        migrations.AddField(
            model_name='pedido_entrada_temp',
            name='empleadosustituto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='empleado.Empleado'),
        ),
    ]