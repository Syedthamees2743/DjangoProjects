from django.contrib import admin
from .models import Train, Ticket, UserProfile

admin.site.register(Train)
admin.site.register(Ticket)
admin.site.register(UserProfile)