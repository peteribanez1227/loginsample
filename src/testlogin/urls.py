from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login_view',),
    path('logout/', views.logout_request, name='logout'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
    path('deleteuser/<int:uid>', views.delete_user, name='deleteuser'),
    path('viewuser/<int:uid>', views.view_user, name='viewuser'),
    path('employee/', views.employee, name='employee'),
    path('uploademployee/', views.upload_employee, name='uploademployee'),
    path('uploadusers/', views.uploadusers, name='uploadusers'),
    path('attendance/', views.attendance, name='attendance'),
    path('disputes/', views.disputes, name='disputes'),
    path('adminpage/', views.adminpage, name='adminpage'),
    path('manageuser/', views.manageuser, name='manageuser'),
    path('creategroup/', views.creategroup, name='creategroup'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
