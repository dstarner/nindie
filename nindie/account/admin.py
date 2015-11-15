from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.


class UserProfile(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

# Define a new User admin
class MyUserAdmin(UserAdmin):
    inlines = (UserProfile,)


admin.site.register(Artist)
admin.site.register(Song)