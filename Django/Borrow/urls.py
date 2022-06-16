from django.urls import path

from . import views

app_name = 'borrow'

urlpatterns = [
    path('manage/', views.show_recordings, name='managePage'),
    path('order/', views.order_book_view, name='orderPage'),
    path('post_del_recording/', views.remove_recording, name="removeRecording"),
    path('post_update_recording/', views.update_recording, name="removeRecording"),
    path('get_borrow_info/', views.pull_borrow_info, name="getBorrowInfo"),
    path('post_borrow_orders/', views.add_recordings, name="postOrders")
]
