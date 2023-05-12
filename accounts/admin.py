from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'user_type', 'image']
    list_filter = ['user_type']
    search_fields = ['user_type']
    list_per_page = 10