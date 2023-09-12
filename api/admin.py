from django.contrib import admin
from .models import Chiste

@admin.register(Chiste)
class ChisteAdmin(admin.ModelAdmin):
    list_display = ('id','texto')