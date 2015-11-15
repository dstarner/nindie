from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^logout/$', views.user_logout, name="logout"),
    url(r'^login/$', views.user_login, name="login")
]
