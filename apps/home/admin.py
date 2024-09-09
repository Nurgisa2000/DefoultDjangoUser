from django.contrib import admin
from django.utils.safestring import mark_safe

from apps.home.models import Post


@admin.register(Post) 
class PostAdmin(admin.ModelAdmin):
    list_display = ['view_image', 'description', 'author']
    list_filter = ['created_at']
    readonly_fields = ['updated_at', 'created_at']

    def view_image(self, obj: Post):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')
        else:
            return 'No image'
