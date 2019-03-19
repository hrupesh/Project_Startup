# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Order, order_total
from django.contrib import admin

# Register your models here.
class order_display(admin.ModelAdmin):
    list_display = ['user_id', 'cart', 'status', 'timeslot', 'timestamp']
    search_fields = ['user_id', 'cart', 'status', 'timeslot']
    #date_hierarchy = ['timestamp', 'timeslot']
    readonly_fields = ['timestamp']

    class meta:
        model = Order

admin.site.register(Order, order_display)


class order_total_display(admin.ModelAdmin):
    list_display = ['order_name', 'total', 'tax_total', 'final_total', 'timestamp']
    search_fields = ['order_name']
    #date_hierarchy = ['timestamp']
    readonly_fields = ['timestamp']

    class meta:
        model = order_total

admin.site.register(order_total, order_total_display)