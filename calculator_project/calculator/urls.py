from django.urls import path
from . import views

urlpatterns = [
    path('', views.step1, name='step1'),
    path('step2/', views.step2, name='step2'),
    path('step3/', views.step3, name='step3'),
    path('result/', views.result, name='result'),
    path('reset/', views.reset, name='reset'),
]