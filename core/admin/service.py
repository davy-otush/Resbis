from django.contrib import admin
from core.models.service import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')