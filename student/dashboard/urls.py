from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("view_classrooms/", views.view_all_classrooms, name="view_classroom"),
    path("create/", views.create_classroom, name="create_classroom"),
    path("join/", views.join_classroom, name="join_classroom"),
    path("create_notifications/", views.create_notifications, name="create_notifications"),
    path("notifications/", views.notify, name="notify"),
]