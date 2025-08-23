from django.contrib import admin
from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ["title", 'author',"counted_view", "status", "created_date", "published_date", ]
    list_filter = ['status', 'author']
    search_fields = ['title', 'content']
    
    
@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name']