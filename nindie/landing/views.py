from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate


def index(request):
    """
    Landing Page for whole Website
    """
    return render(request, "index.html")


def user_login(request):
    user = authenticate(username="JeremySawyer", password="password")
    login(request, user)
    return redirect("accounts:index")


def user_logout(request):
    logout(request)
    return redirect("landing:index")
