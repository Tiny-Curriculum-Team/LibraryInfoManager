from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, get_user_model, authenticate
from .forms import UserLoginForm
from .models import Administrator

ROOT_USER = Administrator.objects.create_user(
    admin_name='Cheese',
    user_name='Breeze',
    password='szqszq1144',
    tel='15941325538'
)


# Create your views here.
def admin_login(request):
    if request.method == 'POST':
        user_login_form = get_user_model()
        if user_login_form:
            data = request.POST
            print(data)
            user = authenticate(username=data['workid'], password=data['password'])
            print(user)
            if user:
                login(request, user)
                return HttpResponse("Success!")
            else:
                return HttpResponse("账号或密码输入有误。请重新输入~")
        else:
            return HttpResponse("账号或密码输入不合法")
    elif request.method == 'GET':
        user_login_form = UserLoginForm()
        context = {'form': user_login_form}
        return render(request, 'static/admin_login.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据")


def admin_logout(request):
    logout(request)
    return HttpResponse("Success!")
