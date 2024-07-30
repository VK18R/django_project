from django.urls import path,include
from . import views

urlpatterns=[
    path("",views.data,name="data"),
    path("login/",views.data,name="data"),
    path("register/",views.data2,name="data2"),
    path("process/",views.submit,name="submit"),
    path("database/",views.my_view,name="my_view"),
]