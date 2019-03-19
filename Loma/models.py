# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from order.models import Order
from user_model.models import address
from products.models import product
#from vendor.models import vendor_daily_PL
from django.db import models
from dp.models import dp_master
import datetime


# Create your models here.

# model of loma_master registration details


class Loma_master(models.Model):
    loma_name = models.CharField(max_length=120)
    loma_email = models.EmailField(max_length=60)
    loma_password = models.CharField(max_length=120)
    loma_permanent_Address = models.CharField(max_length=120)
    city = models.CharField(max_length=30)
    Loma_mandi_name = models.CharField(max_length=120)
    # dropdown hoga mandi ke names mai so ye kisi ko daaalna nahi padega apne app aaaa jayega yaha se
    loma_zone = models.CharField(max_length=120)
    loma_mobile_no = models.IntegerField(default=0.00)
    #description = models.TextField(null=False)
    #price = models.DecimalField(decimal_places=2, max_digits=10, default=19.99)
    loma_slug = models.SlugField(unique=True)
    #Image = models.FileField(upload_to='products/images/', null= True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    

    def __unicode__(self):
        return "id: %s, loma_name: %s, Loma_mandi_name: %s" % (self.id, self.loma_name, self.Loma_mandi_name)

# operation related to the selection purpose of delivery persons by loma.........


class Loma_operation_model(models.Model):
    # username user kaaa toh address yaa order_id waali foreign ki se le lenge
    username = models.CharField(max_length=120)
    user_order_id = models.ForeignKey(
        Order, null=True, on_delete=models.CASCADE)
    user_address = models.ForeignKey(address, on_delete=models.CASCADE)
    loma_Zone = models.ForeignKey(Loma_master, on_delete=models.CASCADE)
    dp_name = models.ForeignKey(dp_master, on_delete=models.CASCADE)

    def __unicode__(self):
        return str(self.id)

# date hireachy lagani he padegi ki alag alag


class Daily_price_list(models.Model):
    price_list_date = models.DateField(auto_now_add=True)
    price_list_time = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    #mandi_id = models.ForeignKey()

    loma_id = models.ForeignKey(Loma_master, on_delete=models.CASCADE)
    #vendor_id = models.ForeignKey(vendor_daily_PL)

# yaha offer and list toh upar foreign key se aaaa jaaaaynge
    offer_price = models.FloatField(default=10.5)
    list_price = models.IntegerField(default=0.00)
    margin = models.FloatField(default=0.00)

    total_available_quantity = models.FloatField(default=50.5)
    rating = models.IntegerField(default=2.5)
    #Total = models.FloatField(default=0.00) ('ye alag table hogi total ke liye')

    def __unicode__(self):
        return self.product.title


# model of price_list which will be approve by loma in daily basis..
class approved_pl_by_loma(models.Model):
    Loma_master = models.ForeignKey(Loma_master, on_delete=models.CASCADE)
    #vendor_id = models.ForeignKey(vendor_daily_PL)
    # only product name by products
    product_name = models.ForeignKey(product, on_delete=models.CASCADE)
    # daily price list se calculated (sabhi kaa avg according to the formula) offer price and list price aaayega
    # ye price approve hokr product mai price models pr jaaakr price btaaa sktaaa hai
    # ye price puraaa caluclated hogaaaa
    cal_offer_price = models.FloatField(null=True)
    #list_price = models.FloatField(null=False)
    verified = models.BooleanField(default=False)

    def __unicode__(self):
        return "product_name: %s | cal_offer_price: %s" % (self.product_name, self.cal_offer_price)


STATUS_CHOICES = (
    ("A", "A"),
    ("P", "P"),
)


class loma_attendance_model(models.Model):
    loma_master = models.ForeignKey(Loma_master, on_delete=models.CASCADE)
    loma_attendance = models.CharField(
        max_length=120, choices=STATUS_CHOICES, default='A')
    today_date = models.DateField(default=datetime.date.today)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    active = models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.loma_master)


class md(models.Model):
    #vendor = models.ForeignKey(vendor_master)
    loma_id = models.ForeignKey(Loma_master, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=100, default='Jaipur')
    Mandi_name = models.CharField(max_length=200)
    # only area name
    locality = models.CharField(max_length=100)
    # proper address
    address = models.CharField(max_length=300)

    def __unicode__(self):
        return self.Mandi_name


class promocode_model(models.Model):
    promocode_id = models.CharField(max_length=5)
    promocode_name = models.CharField(max_length=11)
    valid_from = models.DateTimeField(auto_now=False)
    valid_to = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.promocode_name
