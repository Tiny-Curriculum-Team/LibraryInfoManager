from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book
from Publisher.models import Publisher
from BookType.models import BookType


# Create your views here.
def add_book(request):
    if request.method == 'POST':
        ISBN = request.POST['add_ISBN']
        book_name = request.POST['add_book_name']
        author = request.POST['add_author']
        location = request.POST['add_location']
        status = 'IN'
        book_type = request.POST['add_book_type']
        book_type_id = BookType.objects.filter(book_type_name=book_type).values("BookTypeID")
        publisher = request.POST['add_publisher']
        publisher_id = Publisher.objects.filter(publisher_name=publisher).values("PublisherID")
        item = Book(
            ISBN=ISBN,
            book_name=book_name,
            author=author,
            location=location,
            status=status,
            book_type_id=book_type_id,
            publisher_id=publisher_id,
        )
        item.save()
        messages.info(request, "图书添加成功！")
    return redirect("/bm/")


def remove_book(request):
    if request.method == 'POST':
        del_ISBN = request.POST['del_ISBN']
        try:
            item = Book.objects.filter(ISBN=del_ISBN)
            item.delete()
        except:
            messages.info(request, "图书删除失败！可能原因是已经删除或者不存在该图书！")
            return redirect("/bm/")
        finally:
            messages.info(request, "图书删除成功！")
            return redirect("/bm/")


def pull_book_info(request):
    if request.method == "GET":
        pull_ISBN = request.GET['pull_ISBN']
        query_obj = Book.objects.filter(ISBN=pull_ISBN)
        if query_obj.exists():
            data = {
                "ISBN": query_obj.values("ISBN")[0]["ISBN"],
                "book_name": query_obj.values("book_name")[0]["book_name"],
                "author": query_obj.values("author")[0]["author"],
                "location": query_obj.values("location")[0]["location"],
                "book_type": query_obj.values("book_type__book_type_name")[0]["book_type__book_type_name"],
                "publisher": query_obj.values("publisher__publisher_name")[0]["publisher__publisher_name"],
            }
            return JsonResponse(data)
        else:
            return JsonResponse({})


def update_book(request):
    if request.method == 'POST':
        update_ISBN = request.POST['update_ISBN']
        book_type_name = request.POST['update_book_type']
        publisher_name = request.POST['update_publisher']

        book_type_id = BookType.objects.filter(book_type_name=book_type_name)[0].BookTypeID
        publisher_name = Publisher.objects.filter(publisher_name=publisher_name)[0].PublisherID

        update_obj = Book.objects.get(ISBN=update_ISBN)
        update_obj.ISBN = request.POST['update_ISBN']
        update_obj.book_name = request.POST['update_book_name']
        update_obj.author = request.POST['update_author']
        update_obj.location = request.POST['update_location']
        update_obj.book_type_id = book_type_id
        update_obj.publisher_id = publisher_name

        update_obj.save()

        messages.info(request, "图书信息修改成功！")
        return redirect("/bm/")



def book_view(request):
    current_user = request.user
    if current_user.is_anonymous:
        messages.info(request, "由于您还未登录，故访问被拒绝！")
        return redirect("/sign/in/")
    elif current_user.is_admin:
        books = Book.objects.all().values(
            'ISBN', 'book_name', 'author', 'location', 'status',
            'book_type__book_type_name',
            'publisher__publisher_name'
        )
        return render(request, 'static/ManageBook.html', {'books': books})
    else:
        messages.info(request, "由于您还不是管理员，故访问被拒绝！")
        return redirect("/sign/in/")
