# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-30 15:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cityscore', '0004_auto_20160626_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='entry_date',
            field=models.DateField(default=datetime.date.today, verbose_name=b'Date'),
        ),
        migrations.AlterField(
            model_name='value',
            name='metric',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cityscore.Metric', verbose_name=b'Metric'),
        ),
        migrations.AlterField(
            model_name='value',
            name='val',
            field=models.FloatField(verbose_name=b'Value'),
        ),
    ]
