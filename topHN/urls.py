from django.urls import path
from . import views

app_name="topHN"
urlpatterns=[
    path("", views.stories, name="stories"),
]
