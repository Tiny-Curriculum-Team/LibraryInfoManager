from django.urls import path

from . import views

app_name = 'books'

urlpatterns = [
    path('', views.book_view, name='mb'),
    path('post_addbook/', views.add_book, name='addBook'),
    path('post_delbook/', views.remove_book, name='delBook'),
    path('post_updatebook/', views.update_book, name='updateBook'),
    path('get_book_info/', views.pull_book_info, name='getBookInfo'),
    path('get_book_type_list/', views.pull_book_type_list, name='getBookTypeInfo'),
    path('get_publisher_list/', views.pull_publisher_list, name='getPublisherInfo')
]