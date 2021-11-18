from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home),
    path('properties/',views.properties),
    path('getintouch/',views.getintouch),
    path('loginpage/',views.loginpage),
    path('logoutpage/',views.logoutpage),
    path('register/',views.register),
    path('faq/',views.faq),
    path('requestinfo/',views.requestinfo),
    # path('dashboard/',views.dashboard),
    path('upcoming/',views.upcoming),
    path('performance/',views.performance),
    path('adminhome/',views.adminhome),
    path('addclient/',views.addclient),
    path('viewclients/',views.viewclients),
    path('updateclient/<str:firstname>/', views.updateclient),
    path('deleteclient/<str:firstname>/', views.deleteclient),
    path('addproperty/',views.addproperty),
    path('viewproperties/',views.viewproperties),
    path('property/<str:property_name>/',views.property),
    path('updateproperty/<str:property_name>/', views.updateproperty),
    path('deleteproperty/<str:property_name>/', views.deleteproperty),
    path('source/',views.source),
    path('progress/',views.progress),
    path('errorpage/',views.errorpage),
    path('viewinfo/<str:property_name>/',views.viewinfo),
    path('review/<str:property_name>/',views.review),
    path('reviewlist/',views.reviewlist),
]