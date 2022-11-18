from django.contrib import admin
from .models import Item, Category, Tag
from datetime import datetime


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_price', 'get_average_rating')
    prepopulated_fields = {"slug": ("title",), }


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title']
