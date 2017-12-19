# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.gis.geos import Point

from gnt import models

#creating serializer for Profile model
class ProfileSerializer(serializers.ModelSerializer):
    latitude = serializers.SerializerMethodField()
    longitude = serializers.SerializerMethodField()
 
    class Meta:
        model = models.Profile
        fields = ('id', 'user', 'address', 'phone_number', 'latitude', 'longitude' )  
    def get_latitude(self,obj):
        self.latitude = obj.location.get_coords()[0]
        return self.latitude
    def get_longitude(self,obj):
        self.longitude = obj.location.get_coords()[1]
        return self.longitude
 
#creating serializer for GiveOffer model
class GiveOfferSerializer(serializers.ModelSerializer):
    
    latitude = serializers.SerializerMethodField()
    longitude = serializers.SerializerMethodField()
    giver_name = serializers.SerializerMethodField()
 
    class Meta:
        model = models.GiveOffer
        fields = ('id', 'giver_name', 'item_name', 'offer_started_date', 
                  'offer_end_date', 'note_on_offer', 'properties', 'latitude', 'longitude')
 
    def get_latitude(self,obj):
        self.latitude = obj.giver.location.get_coords()[0]
        return self.latitude
    
    def get_longitude(self,obj):
        self.longitude = obj.giver.location.get_coords()[1]
        return self.longitude
    
    def get_giver_name(self,obj):
        self.giver_name = obj.giver.user.username
        return self.giver_name
    
 

#creating serializer for TakeOffer model
class TakeOfferSerializer(serializers.ModelSerializer):
    latitude = serializers.SerializerMethodField()
    longitude = serializers.SerializerMethodField()
    taker_name = serializers.SerializerMethodField()
    class Meta:
        model = models.TakeOffer
        fields = ('id', 'taker_name','note_from_taker', 'offer_status', 'pickup_timeslots', 'latitude', 'longitude')

    def get_latitude(self,obj):
        self.latitude = obj.taker.location.get_coords()[0]
        return self.latitude
    
    def get_longitude(self,obj):
        self.longitude = obj.taker.location.get_coords()[1]
        return self.longitude
    
    def get_taker_name(self,obj):
        self.taker_name = obj.taker.user.username
        return self.taker_name