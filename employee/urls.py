from django.urls import path
from . import views

urlpatterns = [
    path("", views.employee_index, name="employee_index"),
    path("add", views.employee_add, name="employee_add"),
    # path("new", views.employee_new, name="employee_new"),
    path("<int:pk>/", views.employee_detail, name="employee_detail"),

]