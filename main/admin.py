from django.contrib import admin


from .models import Post
from unfold.admin import ModelAdmin

@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ['title','is_active','created_at']
    search_fields = ('title','desc')
    list_filter = ['created_at', 'is_active']
    