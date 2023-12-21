from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include('django.contrib.auth.urls')),
    path('authentication/', include('authentication.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('class/', include('class.urls')),
    path('notes/', include('notes.urls')),
    path('', include('gallery.urls')),
    path('lost/', include('lost.urls')),
    
    

   
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
