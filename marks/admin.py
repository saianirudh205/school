from django.contrib import admin
from .models import Marks

@admin.register(Marks)
class MarksAdmin(admin.ModelAdmin):
    pass
