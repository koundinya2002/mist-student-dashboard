from django.urls import path
# from .views import UserEditView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns =[
    path("login/", views.login_view, name="login" ),
    path("logout/", views.logout_view, name='logout'),
    path("password/", auth_views.PasswordChangeView.as_view(), name="password")
] 