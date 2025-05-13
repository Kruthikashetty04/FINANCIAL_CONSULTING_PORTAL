from django.db import models

# Create your models here.
    
class EventRegistration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default="default@example.com")
    phone = models.CharField(max_length=15)
    event_name = models.CharField(max_length=200)
    registration_date = models.DateTimeField(auto_now_add=True)