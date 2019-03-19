# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#from Loma.models import Loma_operation_model
from django.db import models

# Create your models here.


class dp_master(models.Model):
    firstname = models.CharField(max_length=250, help_text='Required')
    lastname = models.CharField(max_length=250, help_text='Required')
    username = models.CharField(
        max_length=250, unique=True, help_text='Required')
    email = models.EmailField(max_length=250, help_text='Required')
    contact_no = models.IntegerField(null=True)
    password = models.CharField(max_length=100)
    #vehicle =  models.ForeignKey(dp_vehicle_model)
    slug = models.SlugField(unique=True, null=True)
    #address = models.ForeignKey('address')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    email_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    def __unicode__(self):
        return 'id%s_%s _%s ' % (self.id, self.firstname, self.lastname)


class dp_vehicle_model(models.Model):
    dp = models.ForeignKey(dp_master, on_delete=models.CASCADE)
    vechile_registration_number = models.CharField(max_length=120)
    Image_cv = models.ImageField(null=True)
    Driving_license_image = models.ImageField(null=True)
    licenseno = models.CharField(max_length=120)

    def __unicode__(self):
        return str(self.dp)


STATUS_CHOICES = (
    ("Started", "Started"),
    ("Abandoned", "Abandoned"),
    ("Finished", "Finished"),
)


class Dp_order_model(models.Model):
    dp = models.ForeignKey(dp_master, on_delete=models.CASCADE)
    status_order = models.CharField(
        max_length=120, choices=STATUS_CHOICES, default='started')
    no_of_orders = models.IntegerField(null=False)
    #no_of_orders_cal = no_of_orders_cal()
    # yaha se order kiska hai kyaaa hai ye define kar lenge , foreign key se pura data nikaaaal lenge
    #order_by_loma = models.ForeignKey(Loma_operation_model, null=True, blank=True)
    # yaha se loma kii and order ki info mil jaaayegi hum loma operaton model se information uthaayenge
    ordered_loma_name = models.CharField(max_length=100)
    ordered_loma_zone = models.CharField(max_length=100, null=True)
    order_id = models.CharField(max_length=100)
    Customer_name = models.CharField(max_length=120)
    Customer_address = models.CharField(max_length=120)
    #a = models.ForeignKey(Loma_operation_model)

    def __unicode__(self):
        return str(self.dp)

# def no_of_orders_cal():
#    if (status_order == finished):
#       no_of_order +=1
#       return no_of_order
