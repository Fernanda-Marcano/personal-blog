from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from apps.blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('apps.blog.urls'), name='blog'), 
    path('', views.list_category, name='home')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
