from django.contrib import admin
from .models import Money


@admin.register(Money)
class MoneyAdmin(admin.ModelAdmin):
    list_display = ['amount', 'category','origin', 'created']
    list_filter = ['category','owner','origin']
   
