from django.conf import settings
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import index, login_view, register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name='homepage'),
    path('register/', register, name='register'),
    path('login/',login_view,name='login'),
    # url(r'^/login/$', login_view, name='login'),
    # path('logout/', logout_request, name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
