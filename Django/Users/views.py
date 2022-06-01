from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse


def user_login(request):
    return HttpResponse("Hello, world. You're at the user login index.")


def user_logout(request):
    pass


def user_register(request):
    pass