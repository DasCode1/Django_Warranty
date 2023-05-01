from django.db import models

# Create your models here.

from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib.auth.hashers import make_password , check_password








class Product(models.Model):
    id = models.AutoField(primary_key=True, default = 1,unique=True)
    Product_name = models.CharField(max_length=200)
    Description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    warranty_period = models.IntegerField()
    brought_time =models.DateTimeField(default=timezone.now)
    expiry_time = models.DateTimeField(blank=True)


    
    def save(self, *args, **kwargs):
        self.expiry_time = self.brought_time  + timedelta(days=365*self.warranty_period)
        super(Product, self).save(*args, **kwargs)


class Customer(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=200,blank=False)
    customer_user_name =models.CharField(max_length=200,blank=False)
    customer_password = models.CharField(max_length=200,blank=False)

    def set_password(self, raw_password):
        self.customer_password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)


   

