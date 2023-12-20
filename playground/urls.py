from django.urls import path

from . import views

#  urlConfig
urlpatterns = [
    path('playground/hello', views.say_hello),
]