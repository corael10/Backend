# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-26 14:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0010_auto_20180625_1704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='timestamp',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='file',
            old_name='remark',
            new_name='nombre',
        ),
        migrations.AddField(
            model_name='file',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file_requests_created', to=settings.AUTH_USER_MODEL),
        ),
    ]