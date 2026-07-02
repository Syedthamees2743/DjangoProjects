from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('reset-password/', views.reset_password, name='reset_password'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('train-list/', views.train_list, name='trainlist'),
    path('add-train/', views.add_train, name='addtrain'),
    path('edit-train/<int:pk>/', views.edit_train, name='edit_train'),
    path('update-train/<int:pk>/', views.update_train, name='update_train'),
    path('delete-train/<int:pk>/', views.delete_train, name='delete_train'),
    path('book-ticket/', views.book_ticket, name='bookticket'),
    path('ticket-list/', views.ticket_list, name='ticketlist'),
    path('edit-ticket/<int:pk>/', views.edit_ticket, name='edit_ticket'),
    path('update-ticket/<int:pk>/', views.update_ticket, name='update_ticket'),
    path('cancel-ticket/<int:pk>/', views.cancel_ticket, name='cancel_ticket'),
]