from django.contrib import admin
from rabbfinance.category.models import Category, Origin


@admin.register(Category)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Origin)
class OriginAdmin(admin.ModelAdmin):
    list_display = ['name']
