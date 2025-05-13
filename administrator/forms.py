from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Event, Training, VideoGallery, Blogs,EventRegistration,Feedback

# Event Form
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_host', 'event_date', 'event_time', 'event_description', 'event_link', 'event_thumbnail', 'is_active']

# Training Form
class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ['training_name', 'training_description', 'training_date', 'training_video', 'training_thumbnail']

# Video Gallery Form
class VideoGalleryForm(forms.ModelForm):
    class Meta:
        model = VideoGallery
        fields = ['video_title', 'video_description', 'video', 'video_thumbnail']
        
# Blogs Form
class BlogsForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ['blogs_author', 'title', 'blogs_description', 'sub_title1', 'sub_description1', 'blogs_thumbnail']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']
    
        
class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = EventRegistration
        fields = ['event', 'name', 'phone', 'email', 'description', 'event_date','event_time']
