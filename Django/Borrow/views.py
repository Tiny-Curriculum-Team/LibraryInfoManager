from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Borrow


# Create your views here.
def show_recording(request):
    current_user = request.user
    if current_user.is_anonymous:
        messages.info(request, "由于您还未登录，故访问被拒绝！")
        return redirect("/sign/in/")
    else:
        borrows = Borrow.objects.all().values()
        return render(request, 'static/Borrow.html', {'borrows': borrows, 'isAdmin': current_user.is_admin})


def update_recording(request):
    pass


def query_recording(request):
    pass
