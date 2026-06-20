from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_student, name='add_student'),
    path('list/', views.student_list, name='student_list'),
    path('detail/<int:id>/', views.student_detail, name='student_detail'),
    path('update/<int:id>/', views.update_student, name='update_student'),
]