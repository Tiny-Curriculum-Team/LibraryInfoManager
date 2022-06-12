from django.urls import path

from . import views

app_name = 'borrow'

urlpatterns = [
    path('', views.show_recordings, name='managePage'),
]
