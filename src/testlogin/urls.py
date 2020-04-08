from django.conf import settings
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.defaults import *
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('employee/', views.employee, name='employee'),
    path('uploademployee/', views.upload_employee, name='uploademployee'),
    path('attendance/', views.attendance, name='attendance'),
    path('disputes/', views.disputes, name='disputes'),
    # url(r'^/login/$', views.login_view, name='login'),
    # path('logout/', logout_request, name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
