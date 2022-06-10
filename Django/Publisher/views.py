from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
def identity_check(request):
    current_user = request.user
    if current_user.is_admin():
        return True
    else:
        return False


def add_book_type(request):
    pass


def remove_book_type(request):
    pass


def booktype_view(request):
    if identity_check(request):
        return render(request, 'static/SignIn.html')
    else:
        messages.info(request, "由于您还不是管理员，故访问被拒绝！")
        return redirect("sign/in/")

