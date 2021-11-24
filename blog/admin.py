from django.contrib import admin
from .models import Category, Post, Social


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']

    def has_add_permission(self, request):
        if self.model.objects.count() >= 3:
            return False
        return super().has_add_permission(request)
        
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'show','featured', 'created_at',]
    list_filter = ['show', 'category', 'created_at', 'updated_at']
    list_editable = ['show','featured']
    ordering = ['-updated_at']


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug',  'show', 'created_at',]
    list_filter = ['show', 'created_at', 'updated_at']
    list_editable = ['show']
    ordering = ['-updated_at']
