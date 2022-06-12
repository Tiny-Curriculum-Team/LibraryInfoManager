from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, get_user_model, authenticate
from .forms import UserLoginForm, UserRegisterForm
from .models import User


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        user_login_form = get_user_model()
        if user_login_form:
            data = request.POST
            user = authenticate(username=data['username'], password=data['password'])
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
        return render(request, 'static/SignIn.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据")


def user_logout(request):
    logout(request)
    return HttpResponse("Success!")


def user_register(request):
    if request.method == 'POST':
        user_register_form = UserRegisterForm(data=request.POST)
        if user_register_form.is_valid():
            new_user = user_register_form.save(commit=False)
            new_user.set_password(user_register_form.cleaned_data['password1'])
            new_user.save()
            login(request, new_user)
            return HttpResponse("Signing up succeeded!")
        else:
            return HttpResponse("注册表单输入有误。请重新输入~")
    elif request.method == 'GET':
        user_register_form = UserRegisterForm()
        context = {'form': user_register_form}
        return render(request, 'static/SignUp.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据")


def user_manage(request):
    current_user = request.user
    if current_user.is_anonymous:
        messages.info(request, "由于您还未登录，故访问被拒绝！")
        return redirect("/user/sign_in/")
    elif current_user.is_admin:
        users = User.objects.filter(is_active=True).values(
            'UserID', 'name', 'nickname', 'tel',
            'is_active', 'last_login', 'trustworthiness',
            'max_borrow_day', 'max_borrow_count',
        )
        del_users = User.objects.filter(is_active=False).values(
            'UserID', 'name', 'nickname', 'tel',
            'is_active', 'last_login', 'trustworthiness',
            'max_borrow_day', 'max_borrow_count',
        )
        return render(request, 'static/ManageUsers.html', {'active_users': users, 'inactive_users': del_users})
    else:
        messages.info(request, "由于您还不是管理员，故访问被拒绝！")
        return redirect("/user/sign_in/")


def remove_user(request):
    if request.method == "POST":
        user_operated_id = request.POST['del_UserID']
        print(type(user_operated_id))
        if user_operated_id == '1':
            messages.info(request, "用户删除失败，超级管理员不能被删除！")
        else:
            user = User.objects.get(UserID=user_operated_id)
            if user:
                user.is_active = False
                user.save()
                messages.info(request, "用户删除成功！")
            else:
                messages.info(request, "用户删除失败，可能原因是已经删除或者不存在该用户！")
        return redirect("/user/manage/")


def restore_user(request):
    if request.method == "POST":
        user_operated_id = request.POST['del_UserID']
        if User.objects.filter(UserID=user_operated_id).exists():
            user = User.objects.get(UserID=user_operated_id)
            user.is_active = True
            user.save()
            messages.info(request, "用户恢复成功！")
        else:
            messages.info(request, "用户恢复失败，可能原因是已经恢复或者不存在该用户！")
        return redirect("/user/manage/")


def pull_query_user_info(request):
    if request.method == "GET":
        pull_UserID = request.GET['pull_UserID']
        query_obj = User.objects.filter(UserID=pull_UserID)
        if query_obj.exists():
            query_data = query_obj.values()[0]
            data = {
                "name": query_data["name"],
                "nickname": query_data["nickname"],
                "tel": query_data["tel"],
            }
            return JsonResponse(data)
        else:
            return JsonResponse({})


def update_user(request):
    if request.method == "POST":
        post_data = request.POST
        print("##################", post_data)
        user_to_update = User.objects.get(UserID=int(post_data['UserID']))
        if post_data['update_user_password'] == '':
            pass
        else:
            user_to_update.set_password(post_data['update_user_password'])
        user_to_update.nickname = post_data['update_user_nickname']
        user_to_update.name = post_data['update_user_name']
        user_to_update.tel = post_data['update_user_telephone']
        user_to_update.save()
        messages.info(request, "用户信息修改成功！")
    return redirect("/user/manage/")
##################
# <QueryDict: {
# 'csrfmiddlewaretoken': [''],
# 'UserID': ['2'],
# 'update_user_nickname': ['112312312'],
# 'update_user_password': [''],
# 'update_user_name': ['1232131'],
# 'update_user_telephone': ['12312']
# }>


def query_user(request):
    pass


# def add_user(request):
#     pass
