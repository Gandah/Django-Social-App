# dwitter/urls.py

from django.urls import path, include
from .views import( dashboard, 
profile_list, profile, 
dashboard_v , signout_view, register)


app_name = "gwitter"

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")), #for login/logout/passwordchange/register urls
    path("dashboard/", dashboard_v, name="dashboard_v"),
    path("", dashboard, name="dashboard"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
    path("logout/", signout_view, name="Signout_view"),
    path("register/", register, name="register"),
    # path("password_change/", password_form, name="password_form"),
    # path("accounts/password_change/done", password_form_done, name="password_form_done"),
    # path("login/", login_view, name="login_view"),
    ]
