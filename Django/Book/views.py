from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book


# Create your views here.
def add_book(request):
    pass


def remove_book(request):
    pass


def book_view(request):
    current_user = request.user
    if current_user.is_anonymous:
        messages.info(request, "由于您还未登录，故访问被拒绝！")
        return redirect("/sign/in/")
    elif current_user.is_admin:
        books = Book.objects.all().values(
            'ISBN', 'book_name', 'author', 'location', 'status',
            'book_type__book_type_name',
            'publisher__publisher_name'
        )
        return render(request, 'static/ManageBook.html', {'books': books})
    else:
        messages.info(request, "由于您还不是管理员，故访问被拒绝！")
        return redirect("/sign/in/")
