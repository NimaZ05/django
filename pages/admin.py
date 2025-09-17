from django.contrib import admin
from .models import Contact, Newsletter


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ['name', 'email', 'created_date']
    list_filter = ['email']
    search_fields = ['name', 'message']
@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email', 'created_date'] 
