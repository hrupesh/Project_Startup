# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-03 08:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Loma', '0003_daily_price_list_daily_price_list_approoved_by_loma_loma_operation_model'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='daily_price_list_approoved_by_loma',
            new_name='approved_PL_loma',
        ),
    ]
