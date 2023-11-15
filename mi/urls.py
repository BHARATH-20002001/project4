from mi.views import *
from django.urls import path
app_name = 'something'
urlpatterns = [
    path('rohit/',rohit,name='rohit'),
    path('suryakumar/',suryakumar,name='suryakumar')
]
