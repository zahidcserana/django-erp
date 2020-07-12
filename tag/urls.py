from django.urls import path
from . import views

urlpatterns = [
    path("", views.tag_index, name="tag_index"),
    path("<int:pk>/delete", views.tag_delete, name="tag_delete"),
]
