from django.urls import path

from . import views

app_name = 'admin'

urlpatterns = [
    path('', views.admin_login, name='admin_login'),
]