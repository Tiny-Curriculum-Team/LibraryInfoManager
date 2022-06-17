from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Publisher


# Create your views here.
def add_publisher(request):
    if request.method == 'POST':
        data = request.POST['addPublisher']
        types = data.split(';')
        for book_type in types:
            if book_type == '':
                continue
            item = Publisher(publisher_name=book_type)
            item.save()
        messages.info(request, "出版社添加成功！")
    return redirect("/pubm/")


def remove_publisher(request):
    if request.method == 'POST':
        data = request.POST['delPublisher']
        types = data.split(';')
        for to_del in types:
            if to_del == '':
                continue
            try:
                item = Publisher.objects.get(PublisherID=to_del)
                item.delete()
            except:
                messages.info(request, "出版社删除失败！可能原因是已经删除或者不存在该出版社！")
                return redirect("/pubm/")
        messages.info(request, "出版社删除成功！")
        return redirect("/pubm/")


def publisher_view(request):
    current_user = request.user
    if current_user.is_anonymous:
        messages.info(request, "由于您还未登录，故访问被拒绝！")
        return redirect("/sign/in/")
    elif current_user.is_admin:
        publishers = Publisher.objects.all()
        return render(request, 'static/ManagePublisher.html', {'publishers': publishers, 'isAdmin': current_user.is_admin})
    else:
        messages.info(request, "由于您还不是管理员，故访问被拒绝！")
        return redirect("/sign/in/")

