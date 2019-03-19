# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import  dp_master, dp_vehicle_model, Dp_order_model
from django.contrib import admin

# Register your models here.
admin.site.register(dp_master)


admin.site.register(dp_vehicle_model)


admin.site.register(Dp_order_model)