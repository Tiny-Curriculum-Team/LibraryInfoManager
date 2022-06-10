from django.urls import path

from . import views

app_name = 'books'

urlpatterns = [
    path('', views.book_view, name='mb'),
    path('addbook/', views.add_book, name='addBook'),
    path('delbook/', views.remove_book, name='delBook'),
]