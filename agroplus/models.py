from email.mime import message
from tkinter import Image
from turtle import mode
from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.

class Sell(models.Model):
    SellerName = models.CharField(max_length=40)
    CropName = models.CharField(max_length=20)
    Image = models.ImageField()
    imgpath = models.CharField(max_length=200, default='')
    Price= models.IntegerField(default=0,blank=True,null=True)
    Description = models.TextField(blank=True)
    Quantity = models.IntegerField(default=0,blank=True)
    date = models.DateField(default=datetime.now)
    def __str__(self):
        # price=string(self.Price) 
        return self.CropName+ ' ' + '' + ' ( Seller = ' + self.SellerName +' )'
class price(models.Model):
    CropName = models.CharField(max_length=20)
    Price= models.IntegerField(default=0,blank=True,null=True)
    def __str__(self):
        return self.CropName