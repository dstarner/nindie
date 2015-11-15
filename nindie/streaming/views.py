import os
from django.http import HttpResponse
from django.shortcuts import render
from streaming.lib.xml import xml_artist_list
from nindie.settings import BASE_DIR
from streaming.lib.scraping import get_similar_artists
from streaming.lib.youtuber import search_youtube
from account.models import *
from django.shortcuts import redirect
from account.models import Artist,Song
import random
import json


def load_artists(request,quick_run=0):
    file = request.FILES['file']
    print("Printing List")
    BASE = BASE_DIR
    os.system("touch " + BASE + "/streaming/lib/xmls/" + str(request.user.id) + '.xml')
    with open(BASE + '/streaming/lib/xmls/' + str(request.user.id) + '.xml', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    artists = xml_artist_list(BASE + '/streaming/lib/xmls/' + str(request.user.id) + '.xml')

    for artist_name in artists[:3]:
        count = 0
        if count < 5:
            if artist_name is not None and artist_name is not "":
                artist = Artist.objects.create(name=artist_name)
                print("Finding Major Artist: " + artist.name)
                artist.save()
                for diction in search_youtube(artist_name):
                    song = Song.objects.create(artist=artist, url=diction['url'], title=diction['title'])
                    song.save()
                    print(song.title)
                similar_artists = get_similar_artists(artist_name)
                for similar_artist_name in similar_artists[:3]:
                    similar_artist = Artist.objects.create(name=similar_artist_name)
                    print("Sim Artist: " + similar_artist.name)
                    similar_artist.save()
                    for diction in search_youtube(artist_name)[:3]:
                        similar_song = Song.objects.create(artist=similar_artist, url=diction['url'], title=diction['title'])
                        print(similar_song.title)
                        similar_song.save()
            count += 1
    return redirect("account:index")


def add_artist(request):
    artist_name = request.POST.get("artist", "Null")
    artist = Artist.objects.create(name=artist_name)
    artist.save()
    for diction in search_youtube(artist_name):
        song = Song.objects.create(artist=artist, url=diction['url'], title=diction['title'])
        song.save()
        print(song.title)
    similar_artists = get_similar_artists(artist_name)
    for similar_artist_name in similar_artists[:3]:
        similar_artist = Artist.objects.create(name=similar_artist_name)
        print("Sim Artist: " + similar_artist.name)
        similar_artist.save()
        for diction in search_youtube(artist_name)[:3]:
            similar_song = Song.objects.create(artist=similar_artist, url=diction['url'], title=diction['title'])
            print(similar_song.title)
            similar_song.save()
    return redirect("account:index")


def pick_random(request):
        profile_artists = Artist.objects.all()
        print(profile_artists)
        for artist in profile_artists:
            print(Song.objects.filter(artist=artist).all())
        art_num = random.randrange(0, len(profile_artists))
        artist = profile_artists[art_num]
        songs = Song.objects.filter(artist=artist).all()
        song_num = random.randrange(0, len(songs))
        grabbed_song = songs[song_num]
        return grabbed_song.id


def delete_song(request, song_id):
    response_data = {}

    song = Song.objects.get(id=song_id)
    song.delete()

    new_song = pick_random(request)

    response_data['title'] = new_song.title
    response_data['url'] = new_song.url

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json")


def next_song(request):
    return redirect("account:index")
