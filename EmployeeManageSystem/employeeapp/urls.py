from django.urls import path
from . import views

urlpatterns = [
    path("", views.add_employee, name="add_employee"),
    path("view/", views.view_employee, name="view_employee"),
    path("editemployee/<int:emp_id>/", views.editemployee, name="editemployee"),
    path("updateemployee/<int:emp_id>/", views.updateemployee, name="updateemployee"),
    path("deleteemployee/<int:emp_id>/", views.deleteemployee, name="deleteemployee"),
]
