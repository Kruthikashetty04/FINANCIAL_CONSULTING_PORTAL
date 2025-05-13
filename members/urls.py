from django.urls import path
from .views import *

app_name="members"

urlpatterns = [
     path('publicpage/', publicpage,name='publicpage'),
     
]
