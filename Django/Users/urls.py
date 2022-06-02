from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('in/', views.user_login, name='signin'),
    path('up/', views.user_register, name='signup'),
]