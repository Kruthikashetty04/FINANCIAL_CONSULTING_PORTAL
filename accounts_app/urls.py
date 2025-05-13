from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name = 'accounts_app'

urlpatterns = [
    path('register/', registerpage, name='register'),
    path('login/', loginpage, name='login'),
    path('member-home/', homepage, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]