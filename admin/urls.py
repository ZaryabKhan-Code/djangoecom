from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from . import views
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/',include('ecomerceWeb.urls')),
    path('blog/',include('blog.urls')),
    path('',views.index)
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
