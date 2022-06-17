from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import BookType


# Create your views here.
def add_book_type(request):
    if request.method == 'POST':
        data = request.POST['addType']
        types = data.split(';')
        for book_type in types:
            if book_type == '':
                continue
            item = BookType(book_type_name=book_type)
            item.save()
        messages.info(request, "图书种类添加成功！")
    return redirect("/btm/")


def remove_book_type(request):
    if request.method == 'POST':
        data = request.POST['delType']
        types = data.split(';')
        for to_del in types:
            if to_del == '':
                continue
            try:
                item = BookType.objects.get(BookTypeID=to_del)
                item.delete()
            except:
                messages.info(request, "图书种类删除失败！可能原因是已经删除或者不存在该类！")
                return redirect("/btm/")
        messages.info(request, "图书种类删除成功！")
        return redirect("/btm/")


def booktype_view(request):
    current_user = request.user
    if current_user.is_anonymous:
        messages.info(request, "由于您还未登录，故访问被拒绝！")
        return redirect("/sign/in/")
    elif current_user.is_admin:
        book_types = BookType.objects.all()
        return render(request, 'static/ManageBookType.html', {
            'isOffline': current_user.is_anonymous,
            'booktypes': book_types,
            'isAdmin': current_user.is_admin
        })
    else:
        messages.info(request, "由于您还不是管理员，故访问被拒绝！")
        return redirect("/sign/in/")
