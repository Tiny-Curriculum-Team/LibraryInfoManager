from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Borrow
from Users.models import User


# Create your views here.
def show_recordings(request):
    current_user = request.user
    if current_user.is_anonymous:
        messages.info(request, "由于您还未登录，故访问被拒绝！")
        return redirect("/sign/in/")
    elif current_user.is_admin:
        borrows = Borrow.objects.all().values()
    else:
        user_id = int(request.session.get('_auth_user_id'))
        borrows = Borrow.objects.filter(user_id=user_id).values()
    return render(request, 'static/ManageBorrow.html', {'borrows': borrows, 'isAdmin': current_user.is_admin})


def update_recording(request):
    pass


def remove_recording(request):
    pass


def add_recordings(request):
    pass


def query_recording(request):
    pass
