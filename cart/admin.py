# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import cartitem,  carttotal
from django.contrib import admin

# Register your models here.
class CartItem(admin.ModelAdmin):
    list_display = ['user_id','quantity', 'price']
    search_fields = ['user_id']
    #readonly_fields = ['timestamp', 'updated']


admin.site.register(cartitem, CartItem)


class CartItem(admin.ModelAdmin):
    list_display = ['Total', 'updated']
    #search_fields = ['cart']
    readonly_fields = ['timestamp', 'updated']

admin.site.register(carttotal, CartItem)