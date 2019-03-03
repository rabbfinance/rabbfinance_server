from django.contrib import admin
from rabbfinance.category.models import Category


@admin.register(Category)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name']
