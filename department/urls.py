from django.urls import path
from . import views

urlpatterns = [
    path("", views.department_index, name="department_index"),
    path("<int:pk>/delete", views.department_delete, name="department_delete"),
]
