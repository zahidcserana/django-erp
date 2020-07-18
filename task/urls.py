from django.urls import path
from . import views

urlpatterns = [
    path("", views.task_index, name="task_index"),
    path("add", views.task_add, name="task_add"),
    path("<int:pk>/", views.task_detail, name="task_detail")
]
