from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard/$', views.index, name="index"),
    url(r'^settings/$', views.settings, name="settings"),
    url(r'^signup/step/1/$', views.step_1, name="step_1"),
    url(r'^signup/create/$', views.create_user, name="create_user"),
    url(r'^signup/step/2/$', views.step_2, name="step_2"),
]
