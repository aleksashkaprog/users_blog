from django.contrib import admin

from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'user', 'create_time']


admin.site.register(Post, PostAdmin)
