# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import vendor_master,vendor_daily_PL
from django.contrib import admin

# Register your models here.

#class vendor_M(admin.ModelAdmin):


admin.site.register(vendor_master)
admin.site.register(vendor_daily_PL)