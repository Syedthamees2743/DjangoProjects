from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("addcourse/", views.add_course, name="addcourse"),
    path("StudentPage", views.StudentPage, name="StudentPage"),
    path("AddStudent",views.AddStudent,name = 'AddStudent')
]
