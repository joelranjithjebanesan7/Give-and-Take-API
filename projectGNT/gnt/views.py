# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib.gis.db.models import PointField
from django.contrib.gis.db.models.functions import Distance
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import generics
from rest_framework import mixins


from gnt import models
from gnt.models import  *
from gnt import serializers

# Create your views here.
class Offers(generics.ListCreateAPIView):
    queryset = GiveOffer.objects.all()
    serializer_class = serializers.GiveOfferSerializer
    
class OfferList(generics.ListAPIView):
    serializer_class = serializers.GiveOfferSerializer
    offer_model = serializer_class.Meta.model
    model = serializers.ProfileSerializer.Meta.model
    
    def get_queryset(self):
        username = self.kwargs['username']
        user_profile = self.model.objects\
                       .get(user__username=username)
        user_location = user_profile.location
        available_users = self.model.objects\
                        .annotate(
                            distance=Distance('location',user_location)
                                  )\
                        .filter(
                            distance__lt=500
                                  )\
                        .exclude(
                            user__username=username
                                  )\
                        .order_by('distance')
        queryset = self.offer_model.objects.filter(giver__in=available_users)
        return queryset

#offer details    
class GiveOfferDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = GiveOffer.objects.all()
    serializer_class = serializers.GiveOfferSerializer

class TakeOfferDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = TakeOffer.objects.all()
    serializer_class = serializers.TakeOfferSerializer


class ProfileList(generics.ListCreateAPIView):
    queryset =  Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
  
    

    
    
    
    
    
    

    