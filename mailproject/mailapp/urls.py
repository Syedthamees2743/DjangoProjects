from django.urls import path

from mailapp import views


urlpatterns = [
   path('',views.home,name='home'),
   path('add_mail/', views.add_mail,name='add_mail')
]