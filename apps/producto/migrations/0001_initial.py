# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-29 18:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proveedor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('proveedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proveedor.Proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Precio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_1', models.IntegerField()),
                ('precio_2', models.IntegerField()),
                ('precio_3', models.IntegerField()),
                ('precio_4', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('familia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='producto.Familia')),
                ('marca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='producto.Marca')),
                ('precio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='producto.Precio')),
            ],
        ),
    ]
