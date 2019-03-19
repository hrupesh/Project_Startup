# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import promocode_model, Loma_master, Loma_operation_model, Daily_price_list, approved_pl_by_loma, md, loma_attendance_model
from django.contrib import admin

# Register your models here.



admin.site.register(promocode_model)

####

class loma_master_design(admin.ModelAdmin):
    list_display = ['loma_name','Loma_mandi_name','loma_zone', 'city']
    readonly_fields = ['timestamp', 'updated']
    prepopulated_fields = {"loma_slug": ("loma_name",)}

admin.site.register(Loma_master, loma_master_design)

####    

class Loma_operation_model_design(admin.ModelAdmin):
    list_display = ['username', 'user_order_id', 'user_address', 'loma_Zone', 'dp_name']

admin.site.register(Loma_operation_model, Loma_operation_model_design)

####

admin.site.register(Daily_price_list)

####

admin.site.register(approved_pl_by_loma)

admin.site.register(loma_attendance_model)

admin.site.register(md)