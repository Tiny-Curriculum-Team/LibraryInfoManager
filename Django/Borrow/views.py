from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Borrow


# Create your views here.
def show_recordings(request):
    current_user = request.user
    if current_user.is_anonymous:
        messages.info(request, "由于您还未登录，故访问被拒绝！")
        return redirect("/user/sign_in/")
    elif current_user.is_admin:
        borrows = Borrow.objects.all().values()
    else:
        user_id = int(request.session.get('_auth_user_id'))
        borrows = Borrow.objects.filter(user_id=user_id).values()
    return render(request, 'static/ManageBorrow.html', {'borrows': borrows, 'isAdmin': current_user.is_admin})


def pull_borrow_info(request):
    if request.method == "GET":
        pull_operate_id = request.GET['pull_operate_id']
        query_obj = Borrow.objects.filter(OperationID=pull_operate_id)
        if query_obj.exists():
            data = {
                "oprate_id": query_obj.values("OperationID")[0]["OperationID"],
                "borrow_time": query_obj.values("borrow_time")[0]["borrow_time"],
                "status": query_obj.values("status")[0]["status"],
                "back_time": query_obj.values("give_back_time")[0]["give_back_time"],
                "book_ISBN": query_obj.values("book_id")[0]["book_id"],
                "borrower": query_obj.values("user_id")[0]["user_id"],
            }
            return JsonResponse(data)
        else:
            return JsonResponse({})


def update_recording(request):
    if request.method == 'POST':
        print("###############################", request.POST)
        update_operate_id = int(request.POST['update_operate_id'])
        update_obj = Borrow.objects.get(OperationID=update_operate_id)
        update_obj.status = request.POST['update_status']
        update_obj.save()

        messages.info(request, "借阅信息更新成功！")
        return redirect("/brr/")


def remove_recording(request):
    if request.method == 'POST':
        del_recording = request.POST['del_recording']
        try:
            item = Borrow.objects.filter(ISBN=del_recording)
            item.delete()
        except:
            messages.info(request, "图书删除失败！可能原因是已经删除或者不存在该图书！")
            return redirect("/brr/")
        else:
            messages.info(request, "图书删除成功！")
            return redirect("/brr/")


def add_recordings(request):
    pass


def query_recording(request):
    pass
