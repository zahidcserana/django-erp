from django.urls import path
from . import views

urlpatterns = [
    path("", views.designation_index, name="designation_index"),
    path("<int:pk>/delete", views.designation_delete, name="designation_delete"),
]
