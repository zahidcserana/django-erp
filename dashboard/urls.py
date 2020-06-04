from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard_index, name="dashboard_index"),
    path("user-login", views.dashboard_index, name="user_login"),
]
