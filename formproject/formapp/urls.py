from django.urls import path

from formapp import views


urlpatterns = [
    path('',views.home,name='home'),
    path('add_employye',views.add_employye,name='add_employye'),
    path('show_employee',views.show_employee,name='show_employee'),
    path('edit_employee/<int:pk>',views.edit_employee,name='edit_employee')
]