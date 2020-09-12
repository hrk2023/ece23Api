from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("adduser/",views.addUser, name="adduser"),
    path("delete/<user>",views.deleteUser, name="deleteUser"),
    path("update/<userId>",views.updateUser, name="updateUser"),
    path("details/", views.details, name="details"),
    path("detaileduser/<user>", views.detailedUser, name='detaileduser'),
]
