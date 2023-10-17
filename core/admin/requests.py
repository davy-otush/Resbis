from django.contrib import admin
from core.models.requests import Requests

@admin.register(Requests)
class RequestsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'message', 'email', 'telephone')