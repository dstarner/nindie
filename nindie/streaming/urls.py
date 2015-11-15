from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^signup/step/(?P<quick_run>[0-9])/$', views.load_artists, name="load_artists"),
    url(r'^delete/(?P<song_id>[0-9])/$', views.delete_song, name="delete_song"),
    url(r"^pick/new/$", views.next_song, name="new_song"),
    url(r"^add/artist/$", views.add_artist, name="add_artist")
]