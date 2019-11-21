from django.urls import path

from . import views

urlpatterns = [
    path('mailindex', views.subscribe),
]
