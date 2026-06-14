from django.urls import  path
from firstapp import views

urlpatterns = [
    path('',views.indexpage,name='indexpage'),
    path('secondpage',views.secondpage,name='secondpage')
]
