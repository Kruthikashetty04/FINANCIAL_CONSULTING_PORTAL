from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Blogs, Event, Training, VideoGallery, Feedback, MemberProfile,EventRegistration

# Register CustomUser with UserAdmin (only if it's not already registered)
if not admin.site.is_registered(CustomUser):
    @admin.register(CustomUser)
    class CustomUserAdmin(UserAdmin):
        list_display = ("username", "email", "first_name", "last_name", "is_staff", "age", "gender", "contact_number", "aadhaar_number")
        fieldsets = UserAdmin.fieldsets + (
            ("Additional Info", {"fields": ("age", "gender", "contact_number", "aadhaar_number")}),
        )
        add_fieldsets = UserAdmin.add_fieldsets + (
            (None, {
                'classes': ('wide',),
                'fields': ('username', 'email', 'password1', 'password2', 'age', 'gender', 'contact_number', 'aadhaar_number'),
            }),
        )

# Register MemberProfile model
@admin.register(MemberProfile)
class MemberProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "aadhaar", "age", "contact_number", "gender")
    search_fields = ("user__username", "aadhaar", "contact_number")
    list_filter = ("gender",)

# Register other models with the admin site
admin.site.register(Event)
admin.site.register(Training)
admin.site.register(Blogs)

# Register VideoGallery with a custom admin interface
@admin.register(VideoGallery)
class VideoGalleryAdmin(admin.ModelAdmin):
    list_display = ("video_title", "uploaded_at")
    search_fields = ("video_title",)
    list_filter = ("uploaded_at",)

@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ['user', 'event', 'name', 'phone', 'email', 'registered_at']
    search_fields = ['user__username', 'name', 'email', 'event__event_name']
    list_filter = ['event', 'registered_at']
    
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message') 
    search_fields = ('name', 'email', 'message')
  