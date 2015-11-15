import json
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

#######################
# Dashboard & Settings#
# #####################
from account.lib.helpers import generate
from account.models import Profile, Song
from streaming.views import pick_random


@login_required
def index(request):
    video_id = pick_random(request)
    video = Song.objects.get(id=video_id)
    video.last_played = 0
    video.save()
    request.user.profile.songs_played += 1
    request.user.profile.save()
    print(request.user.profile.songs_played)
    last_ten = Song.objects.order_by('last_played').all()
    print(video.title + " " + video.url)
    for each in last_ten:
        each.last_played += 1
        each.save()
    if request.user.profile.songs_played < 10:
        last_to_show = request.user.profile.songs_played
    else:
        last_to_show = 10
    return render(request, "dashboard_index.html", {'song': video, 'previous': last_ten[:last_to_show]})


@login_required
def settings(request):
    return render(request, "settings.html")


# ################
# Sign Up Methods#
# ################


def step_1(request):
    return render(request, "step1.html", {'step': 1})


def create_user(request):
    name = request.POST.get('name', 'no name')
    names = name.split(" ")
    name = name.replace(" ", "")
    first = names[0]
    last = names[1]
    email = request.POST.get("email", "example@mail.com")
    password = request.POST.get("password", "HelloWorld1")
    new_user = User.objects.create_superuser(username=name, first_name=first, last_name=last, email=email, password=password)
    new_user.save()
    # Create Profile
    age = request.POST.get("age", "18")
    profile = Profile.objects.create(age=age, password_reset_code=generate(), user=new_user)
    profile.save()
    user = authenticate(username=name, password=password)
    login(request, user)
    return redirect("account:step_2")


@login_required
def step_2(request):
    # Have them upload iTunes XML file
    return render(request, "step2.html", {'step': 2})
