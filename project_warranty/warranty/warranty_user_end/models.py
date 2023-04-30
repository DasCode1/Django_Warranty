from django.db import models

# Create your models here.

from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta


class Product(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Product_name = models.CharField(max_length=200)
    Description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    warranty_period = models.IntegerField()
    brought_time =models.DateTimeField(default=timezone.now)
    expiry_time = models.DateTimeField(blank=True)


    
    def save(self, *args, **kwargs):
        self.expiry_time = self.brought_time  + timedelta(days=365*self.warranty_period)
        super(Product, self).save(*args, **kwargs)



    