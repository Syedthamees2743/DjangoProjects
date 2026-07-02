
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login_view/', views.login_view, name='login_view'),
    path('signup_view/', views.signup_view, name='signup_view'),
    path('signup/create/', views.usercreate, name='usercreate'),
    path('about/', views.about, name='about'),

    path('user_login', views.user_login, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout')
]