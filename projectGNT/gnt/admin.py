# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.gis import admin
from gnt.models import *

# Register your models here.
""" for admin site interface including the model 
                      with django admin site """
admin.site.register(GiveOffer)
admin.site.register(TakeOffer)
admin.site.register(Profile, admin.OSMGeoAdmin)
