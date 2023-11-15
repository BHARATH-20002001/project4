from csk.views import *
from django.urls import path
app_name = 'something'
urlpatterns = [
    path('msd/',msd,name='msd'),
    path('raina/',raina,name='raina'),
    path('jaddu/',jaddu,name='jaddu'),
]
