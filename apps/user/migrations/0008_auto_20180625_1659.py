# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-25 23:59
from __future__ import unicode_literals

import apps.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20180625_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(storage=apps.storage.OverwriteStorage(), upload_to=''),
        ),
    ]
