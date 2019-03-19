# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import product, product_Image, product_price, product_discount, product_promocode_model
from django.contrib import admin

#Register your models here.

class productt(admin.ModelAdmin):
    list_display = ['title', 'updated']
    search_fields = ['title']
    readonly_fields = ['updated']
    prepopulated_fields = {"slug": ("title",)}

    class meta:
        model = product

admin.site.register(product, productt)



admin.site.register(product_Image)

admin.site.register(product_price)

class discount(admin.ModelAdmin):
    list_display = ['product', 'Offer_in_percentage','lastupdated']
    list_editable = ['Offer_in_percentage']
    search_fields = ['product', 'Offer_in percentage']
    date_hierarchy = 'lastupdated'
    readonly_fields = ['lastupdated']

    class meta:
        model = product_discount

admin.site.register(product_discount, discount)

admin.site.register(product_promocode_model)

'''
class Daily_price_listt(admin.ModelAdmin):
    list_display = ['product', 'vendor_id','offer_price', 'list_price', 'margin', 'total_available_quantity', 'rating']
    search_fields = ['product', 'vendor_id', 'offerprice']
    date_hierarchy = 'price_list_date'
    readonly_fields = ['price_list_date', 'price_list_time']

    class meta:
        model = Daily_price_list


admin.site.register(Daily_price_list, Daily_price_listt)
'''

