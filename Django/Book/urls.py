from django.urls import path

from . import views

app_name = 'books'

urlpatterns = [
    path('', views.book_view, name='mb'),
    path('post_addbook/', views.add_book, name='addBook'),
    path('post_delbook/', views.remove_book, name='delBook'),
    path('post_updatebook/', views.update_book, name='updateBook'),
    path('get_book_info/', views.pull_book_info, name='getBookInfo'),
]