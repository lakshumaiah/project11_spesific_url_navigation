from django.urls import path
from rcb.views import *
app_name='rcbs'
urlpatterns=[
    path('virat/',virat,name='virat'),
]