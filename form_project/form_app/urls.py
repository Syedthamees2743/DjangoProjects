from django.urls import path
from . import views

app_name = 'form_app'

urlpatterns = [
    path('', views.form_page, name='form'),
    path('preview/', views.display_page, name='display'),
    path('edit/', views.edit_page, name='edit'),
    path('confirm/', views.confirm_page, name='confirm'),
]