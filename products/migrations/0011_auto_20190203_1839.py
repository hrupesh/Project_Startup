# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-03 13:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_product_price_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_discount',
            old_name='Offer',
            new_name='Offer_in_percentage',
        ),
    ]
