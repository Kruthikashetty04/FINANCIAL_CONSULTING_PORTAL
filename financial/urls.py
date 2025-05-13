from django.contrib import admin
from django.urls import path, include
from .views import home, design
from administrator.views import member_dashboard, admin_home  # 👈 Import both views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts_app.urls')),
    path('members/', include(('members.urls', 'member'), namespace='member')),
    path('', design, name='design'),
    path('administrator/', include('administrator.urls')),
    path('member-dashboard/', member_dashboard, name='member-dashboard'),
    path('admin-home/', admin_home, name='admin-home'),  
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
