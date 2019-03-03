from django.contrib import admin
from .models import Money

@admin.register(Money)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['amount','category']

