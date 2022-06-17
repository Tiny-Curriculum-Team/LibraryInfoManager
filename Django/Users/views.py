from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, get_user_model, authenticate
import datetime
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
                messages.info(request, "登录成功!")
                return redirect("/")
            else:
                messages.error(request, "账号或密码输入有误。请重新输入~")
        else:
            messages.error(request, "账号或密码输入不合法")
        return redirect("/user/sign_in/")
    elif request.method == 'GET':
        user_login_form = UserLoginForm()
        context = {'form': user_login_form}
        return render(request, 'static/SignIn.html', context)
    else:
        messages.error(request, "请使用GET或POST请求数据")
        return redirect("/user/sign_in/")


def user_logout(request):
    logout(request)
    messages.info(request, "登出成功!")
    return redirect("/")


def user_register(request):
    if request.method == 'POST':
        user_register_form = UserRegisterForm(data=request.POST)
        if user_register_form.is_valid():
            new_user = user_register_form.save(commit=False)
            new_user.set_password(user_register_form.cleaned_data['password1'])
            new_user.save()
            login(request, new_user)
            messages.info(request, "注册成功！")
        else:
            messages.info(request, "注册表单输入有误。请重新输入~")
        return redirect("/user/sign_in/")
    elif request.method == 'GET':
        user_register_form = UserRegisterForm()
        context = {'form': user_register_form}
        return render(request, 'static/SignUp.html', context)
    else:
        messages.error(request, "请使用GET或POST请求数据")
        return redirect("/user/sign_in/")


def user_manage(request):
    current_user = request.user
    condition_u = dict()
    condition_d = dict()
    print(request.POST)
    if current_user.is_anonymous:
        messages.info(request, "由于您还未登录，故访问被拒绝！")
        return redirect("/user/sign_in/")
    elif current_user.is_admin:
        condition_u['is_active'] = True
        condition_d['is_active'] = False
    else:
        messages.info(request, "由于您还不是管理员，故访问被拒绝！")
        return redirect("/user/sign_in/")
    try:
        user_id = request.POST['user_id']
        user_name = request.POST['user_name']
        name = request.POST['name']
        phone = request.POST['phone']
        time = request.POST['time']
        min_point = request.POST['min_point']
        max_point = request.POST['max_point']
        if user_id:
            condition_d['UserID'] = int(user_id)
            condition_u['UserID'] = int(user_id)
        if user_name:
            condition_d["name__icontains"] = user_name
            condition_u["name__icontains"] = user_name
        if name:
            condition_u["nickname__icontains"] = name
            condition_d["nickname__icontains"] = name
        if phone:
            condition_d["tel"] = phone
            condition_u["tel"] = phone
        if time:
            now = datetime.datetime.now()
            end = now - datetime.timedelta(days=int(time))
            condition_u["last_login__range"] = (end, now)
            condition_d["last_login__range"] = (end, now)
        if min_point:
            condition_d["trustworthiness__gte"] = int(min_point)
            condition_u["trustworthiness__gte"] = int(min_point)
        if max_point:
            condition_d["trustworthiness__lte"] = int(max_point)
            condition_u["trustworthiness__lte"] = int(max_point)
    except Exception as e:
        print(e)
    users = User.objects.filter(**condition_u).values(
        'UserID', 'name', 'nickname', 'tel',
        'is_active', 'last_login', 'trustworthiness',
        'max_borrow_day', 'max_borrow_count')
    # print(users)
    del_users = User.objects.filter(**condition_d).values(
        'UserID', 'name', 'nickname', 'tel',
        'is_active', 'last_login', 'trustworthiness',
        'max_borrow_day', 'max_borrow_count')
    return render(request, 'static/ManageUsers.html', {
        'isOffline': current_user.is_anonymous,
        'active_users': users,
        'inactive_users': del_users,
        'isAdmin': current_user.is_admin
    })


def remove_user(request):
    if request.method == "POST":
        user_operated_id = request.POST['del_UserID']
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


def user_profile_view(request):
    current_user = request.user
    if current_user.is_anonymous:
        messages.info(request, "您还未登录，请先登录！")
        return redirect("/user/sign_in/")
    elif current_user.is_admin:
        user = User.objects.filter(UserID=current_user.UserID).values(
            'UserID', 'name', 'nickname', 'tel', 'last_login'
        )
    else:
        user = User.objects.filter(UserID=current_user.UserID).values(
            'UserID', 'name', 'nickname', 'tel',
            'last_login', 'trustworthiness',
            'max_borrow_day', 'max_borrow_count',
        )
    return render(request, 'static/UserProfile.html', {
        'isOffline': current_user.is_anonymous,
        'User': user[0],
        'isAdmin': current_user.is_admin
    })


def update_user_profile(request):
    if request.method == "POST":
        user_id = int(request.user.UserID)
        user = User.objects.get(UserID=user_id)
        update_data = request.POST
        user.nickname = update_data['nickname']
        user.name = update_data['name']
        user.tel = update_data['tele']
        user.save()
    return JsonResponse({"success": True})


def update_user_password(request):
    if request.method == "POST":
        user_id = int(request.user.UserID)
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        user = authenticate(username=user_id, password=old_password)
        if user is not None:
            user = User.objects.get(UserID=user_id)
            user.set_password(new_password)
            user.save()
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False})
