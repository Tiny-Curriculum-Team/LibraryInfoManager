from django.urls import path

from . import views

app_name = 'mainpanel'

urlpatterns = [
    path('', views.show, name='mainPage'),
]
