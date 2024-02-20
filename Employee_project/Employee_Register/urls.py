from django.urls import path
from . import views

urlpatterns=[
    path('',views.employee_from),
    path('d/',views.employee_list),
]