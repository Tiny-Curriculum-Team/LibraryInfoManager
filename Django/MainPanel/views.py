from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
def show(request):
    if request.user.is_anonymous:
        messages.info(request, "您还未登录，请先登录！")
        return redirect("/user/sign_in/")
    user = request.user
    return render(request, "static/MainPanel.html", {"isAdmin": user.is_admin})
