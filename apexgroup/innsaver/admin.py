from django.contrib import admin
from .models import Human

# Register your models here.
@admin.register(Human)
class HumanAdmin(admin.ModelAdmin):
    list_display = ['surname', 'firstName', 'patronymic', 'adress', 'phoneNumber']
    search_fields = ['surname', 'firstName']