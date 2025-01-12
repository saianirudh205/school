from django.contrib import admin
from .models import Class

@admin.register(Class)
class ClassesAdmin(admin.ModelAdmin):
    pass
