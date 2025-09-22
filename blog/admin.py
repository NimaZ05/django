from django.contrib import admin
from .models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ["title", 'author', "counted_view",
                    "status", "created_date", "published_date", ]
    list_filter = ['status', 'author']
    search_fields = ['title', 'content']
    summernote_fields = ('content',)

@admin.action(description="Approve selected comments")
def approve_comments(modeladmin, request, queryset):
    queryset.update(approved=True)   
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ["name", "post", "created_date", "approved"]
    list_filter = ['post', 'approved']
    search_fields = ['name', 'post']
    actions = [approve_comments]


@admin.register(Category)
class CatgoryAdmin(admin.ModelAdmin):
    list_display = ['name']
