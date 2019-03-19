# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from user_model.models import register_model
from products.models import product
from cart.models import cartitem
#from Loma.models import promocode_model
from django.db import models

# Create your models here.

STATUS_CHOICES = (
    ("Started", "Started"),
    ("Abandoned", "Abandoned"),
    ("Finished", "Finished"),
)

timeslot_CHOICES = (
    ("Anytime", "Anytime"),
    ("first_slot", "7:00am - 10:00am"),
    ("secand_slot", "10:am - 1:00pm"),
    ("third_slot", "1:00pm - 4:00pm"),
    ("fourth_slot", "4:00pm - 7:00pm"),
    ("fifth_slot", "7:00pm - 9:00pm"),
)


class Order(models.Model):
    user_id = models.ForeignKey(register_model, on_delete=models.CASCADE)
    cart = models.ForeignKey(cartitem, null=True, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=120, choices=STATUS_CHOICES, default="STARTED")
    #order_total = models.ForeignKey('order_total', null = True)
    timeslot = models.CharField(
        max_length=120, choices=timeslot_CHOICES, default="Any-time")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    #dp  = models.ForeignKey()
    #updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        # jo order id banegi
        # order_id aaayegi yaha
        # return str(self.order_id)
        return str(self.cart)


class order_total(models.Model):
    # total without promocode
    # order_id banayenge jab hum code karenge
    # id apan 'uuid' se bnayenge 128 bit kii integer sedhaa
    #order_id = models.CharField(max_length=120)
    order_name = models.ForeignKey('Order', on_delete=models.CASCADE)
    total = models.DecimalField(default=19.99, max_digits=10, decimal_places=2)
    #promocode = models.ForeignKey(promocode_model, blank = True)
    tax_total = models.DecimalField(
        default=0.00, max_digits=10, decimal_places=2)
    # total with promocode
    final_total = models.DecimalField(
        default=0.00, max_digits=10, decimal_places=2)
    #timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return str(self.order_name)
