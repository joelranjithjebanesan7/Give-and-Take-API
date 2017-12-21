# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.db.models.fields import DateTimeField
from django.contrib.postgres.fields import JSONField
from django.contrib.postgres.fields import ArrayField
# Create your models here.

STATUS_CHOICES = (('pending', 'pending'),('accepted', 'accepted'),('rejected','rejected'))

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length = 12)
    location = models.PointField(null=True,blank=True)
    def __str__(self):
       return  self.user.username
   
class GiveOffer(models.Model):
    giver = models.ForeignKey(Profile)
    item_name = models.CharField(max_length=25)
    offer_started_date = models.DateTimeField()
    offer_end_date = models.DateTimeField()
    note_on_offer = models.TextField()
    offer_status = models.CharField(choices = STATUS_CHOICES, max_length=200,blank=True)
    accepted_taker =models.ForeignKey("Takeoffer",blank=True,null=True)
    properties = JSONField()
    def __str__(self):
       return  self.item_name

class TakeOffer(models.Model):
    taker = models.ForeignKey(Profile)
    offer_taken = models.ForeignKey(GiveOffer,null=True)
    note_from_taker = models.CharField(max_length=200)   
    offer_status =  models.CharField(choices = STATUS_CHOICES, max_length=200)    
    pickup_timeslot = JSONField()
    def __str__(self):
        return  self.taker.user.username