
from django.urls import path

from crudapp import views

urlpatterns = [

    path('',views.addproductspage,name='addproductpage'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('viewproduct',views.viewproduct,name='viewproduct'),
    path('editproduct/<int:pk>',views.editproduct,name='editproduct'),
    path('editpage/<int:pk>',views.editpage,name='editpage'),
    path('deleteproduct/<int:pk>',views.deleteproduct,name='deleteproduct')
]