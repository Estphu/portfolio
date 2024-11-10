from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView, name="index"),
    path("load-more/", views.load_more_content, name="load_more_content"),
]
