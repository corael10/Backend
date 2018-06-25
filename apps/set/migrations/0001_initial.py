# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-27 21:54
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chipset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('model', models.CharField(blank=True, max_length=50, null=True)),
                ('year', models.CharField(blank=True, max_length=50, null=True)),
                ('serie', models.CharField(blank=True, max_length=50, null=True)),
                ('infolink', models.CharField(blank=True, max_length=50, null=True)),
                ('psid', models.CharField(blank=True, max_length=50, null=True)),
                ('url', models.TextField(blank=True, null=True)),
                ('statuspreotn', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChipsetStatusPreotn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chipset', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='chipsetstatuspreotn_requests_created', to='set.Chipset')),
            ],
        ),
        migrations.CreateModel(
            name='Firmware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firmware', models.CharField(max_length=50)),
                ('firmware_number', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='HistVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('infolink', models.CharField(blank=True, max_length=50, null=True)),
                ('chipset', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='set.Chipset')),
                ('firmware_set', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='histversion_requests_created', to='set.Firmware')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='histversion_requests_created', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StatusPreotn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_i', models.DateField()),
                ('date_f', models.DateField()),
                ('status', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='chipsetstatuspreotn',
            name='firmware',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='chipsetstatuspreotn_requests_created', to='set.Firmware'),
        ),
        migrations.AddField(
            model_name='chipsetstatuspreotn',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='chipsetstatuspreotn_requests_created', to='set.StatusPreotn'),
        ),
        migrations.AddField(
            model_name='chipset',
            name='firmware_set',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='chipset_requests_created', to='set.Firmware'),
        ),
        migrations.AddField(
            model_name='chipset',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='chipset_requests_created', to='project.Project'),
        ),
    ]