# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-26 22:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(blank=True, max_length=50, null=True)),
                ('saldo', models.IntegerField(blank=True)),
                ('telefono', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_contra', models.DateField(default=datetime.date.today)),
                ('estatus', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
