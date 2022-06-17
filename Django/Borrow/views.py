import datetime

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta
import json
from django.conf import settings
from .models import Borrow
from Book.models import Book
from Users.models import User


# Create your views here.
def show_recordings(request):
    current_user = request.user
    conditions = dict()
    if current_user.is_anonymous:
        messages.info(request, "由于您还未登录，故访问被拒绝！")
        return redirect("/user/sign_in/")
    elif not current_user.is_admin:
        user_id = int(request.session.get('_auth_user_id'))
        conditions['user_id'] = user_id
    try:
        time = request.POST['time']
        state = request.POST['state']
        book = request.POST['book']
        person = request.POST['person']
        if time:
            now = datetime.datetime.now()
            end = now - datetime.timedelta(days=int(time))
            conditions['borrow_time__range'] = (end, now)
        if state != '不限':
            conditions['status'] = state
        if book:
            conditions['book_id'] = book
        if person:
            conditions['user_id'] = person
    except Exception as e:
        print(e)
    borrows = Borrow.objects.filter(**conditions).values()
    return render(request, 'static/ManageBorrow.html', {
        'isOffline': current_user.is_anonymous,
        'borrows': borrows,
        'isAdmin': current_user.is_admin
    })


def order_book_view(request):
    current_user = request.user
    if current_user.is_anonymous:
        messages.info(request, "由于您还未登录，故访问被拒绝！")
        return redirect("/user/sign_in/")
    else:
        books = Book.objects.all().values(
            'ISBN', 'book_name', 'author', 'location', 'status',
            'book_type__book_type_name',
            'publisher__publisher_name',
        )
        return render(request, 'static/OrderBook.html', {
            'isOffline': current_user.is_anonymous,
            'books': books,
            'isAdmin': current_user.is_admin
        })


def pull_borrow_info(request):
    if request.method == "GET":
        pull_operate_id = request.GET['pull_operate_id']
        if not pull_operate_id:
            return JsonResponse({})
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
        update_operate_id = int(request.POST['update_operate_id'])
        update_status = request.POST['update_status']
        book_id = request.POST['update_book_ISBN']

        update_obj = Borrow.objects.get(OperationID=update_operate_id)
        update_obj.status = update_status
        update_obj.save()

        messages.info(request, "借阅信息更新成功！")
        return redirect("/brr/manage/")


def remove_recording(request):
    if request.method == 'POST':
        del_recording = int(request.POST['del_recording'])
        try:
            item = Borrow.objects.filter(OperationID=del_recording)
            item.delete()
        except:
            messages.info(request, "图书删除失败！可能原因是已经删除或者不存在该图书！")
            return redirect("/brr/manage/")
        else:
            messages.info(request, "图书删除成功！")
            return redirect("/brr/manage/")


def add_recordings(request):
    if request.method == "POST":
        days_and_items = list(json.loads(json.dumps(request.POST)).values())
        user_id = int(request.user.UserID)
        borrow_days = int(days_and_items[0])
        selected = days_and_items[1:]

        number_of_books = len(selected)
        max_borrow_day = int(User.objects.filter(UserID=user_id).values("max_borrow_day")[0]["max_borrow_day"])
        max_borrow_count = int(User.objects.filter(UserID=user_id).values("max_borrow_count")[0]["max_borrow_count"])

        if number_of_books <= max_borrow_count and borrow_days <= max_borrow_day:
            give_back_time = now() + timedelta(days=borrow_days)
            for book_id in selected:
                borrow_item = Borrow(
                    give_back_time=give_back_time,
                    book_id=book_id,
                    user_id=user_id
                )
                borrow_item.save()
            return JsonResponse({"success": True})
        else:
            return JsonResponse({
                "success": False,
                "max_borrow_day": max_borrow_day,
                "max_borrow_count": max_borrow_count
            })
    return redirect("/brr/order/")



@receiver(post_save, sender=Borrow)
def trigger_update_book_status(sender, instance, **kwargs):
    book_item = Book.objects.get(ISBN=instance.book_id)
    if instance.status == '归还' or instance.status == '损坏':
        book_item.status = 'IN'
    else:
        book_item.status = 'OUT'
    book_item.save()

    user_id = instance.user_id
    user = User.objects.get(UserID=user_id)
    if instance.status == '归还' and user.trustworthiness < 100:
        user.trustworthiness += 1
    elif instance.status == '损坏' and user.trustworthiness > 0:
        user.trustworthiness -= 25
    elif instance.status == '丢失' and user.trustworthiness > 0:
        user.trustworthiness -= 50
    elif instance.status == '迟交' and user.trustworthiness > 0:
        user.trustworthiness -= 10
    user.trustworthiness = max(0, user.trustworthiness)

    user.max_borrow_day = int(user.trustworthiness / 100 * settings.MAX_BORROW_DAY)
    user.max_borrow_count = int(user.trustworthiness / 100 * settings.MAX_BORROW_COUNT)
    user.save()


def query_recording(request):
    pass
