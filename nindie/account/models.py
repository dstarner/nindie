from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User)
    password_reset_code = models.CharField(max_length=100, default="")
    age = models.CharField(max_length=8, default="")
    songs_played = models.IntegerField(default=0)

    def __unicode__(self):
        return self.user.username

# Artist
class Artist(models.Model):
    name = models.CharField(max_length=64, default="")

    def __unicode__(self):
        return self.name

# Song
class Song(models.Model):
    artist = models.ForeignKey(Artist, null=True)
    url = models.CharField(max_length=256, default="")
    title = models.CharField(max_length=64, default="")
    last_played = models.IntegerField(default=0)
