from django.urls import path
from . import views

urlpatterns = [
    path("", views.department_index, name="department_index"),
]
