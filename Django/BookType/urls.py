from django.urls import path

from . import views

app_name = 'book_types'

urlpatterns = [
    path('', views.booktype_view, name='mbt'),
    path('post_addbooktype/', views.add_book_type, name='addType'),
    path('post_delbooktype/', views.remove_book_type, name='delType'),
]