from django.urls import path
from csk.views import *

app_name='csks'

urlpatterns=[
    path('dhoni/',dhoni,name='dhoni'),
]