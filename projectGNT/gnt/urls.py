from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include
from django.contrib.auth import views as auth_views

from gnt import views

urlpatterns = format_suffix_patterns([

    url(r'^gnt/$',views.Offers.as_view(), name='offers'),
    url(r'^gnt/profiles/$',views.ProfileList.as_view(),name='profile_list'),
    url(r'^gnt/offer/(?P<pk>[0-9]+)/$',views.GiveOfferDetails.as_view(),name='offer-details'),
    url(r'^gnt/takeoffer/$',views.TakeOfferList.as_view(),name='takeoffer-list'),
    url(r'^gnt/takeoffer/(?P<pk>[0-9]+)$',views.TakeOfferDetails.as_view(),name='takeoffer-details'),
    url(r'^gnt/(?P<username>[a-z]+)/$',views.OfferList.as_view(),name='offer-list'), 
    #url(r'^gnt/approvedoffer/$',views.OfferApproval.as_view(),name='Approvedoffer-list')
    ])

# Login and logout views for the browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
