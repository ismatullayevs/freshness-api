from django.contrib import admin
from .models import Item, Category
from datetime import datetime


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_price')
    prepopulated_fields = {"slug": ("title",), }


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
