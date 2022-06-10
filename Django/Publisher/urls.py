from django.urls import path

from . import views

app_name = 'publishers'

urlpatterns = [
    path('', views.publisher_view, name='mp'),
    path('post_addpublisher/', views.add_publisher, name='addPublisher'),
    path('post_delpublisher/', views.remove_publisher, name='delPublisher'),
]