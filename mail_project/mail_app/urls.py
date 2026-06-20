from django.urls import path
from mail_app.views import add_mail

urlpatterns = [
    path('', add_mail, name='add_mail'),
]