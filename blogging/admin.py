from django.contrib import admin

from blogging.models import Post, Category

admin.site.register(Post)
admin.site.register(Category)

class PostAdmin(admin.ModelAdmin):
    fields = (
        'title', 'text', 'author', 'created_date', 'modified_date', 'published_date'
    )

class Category(admin.ModelAdmin):
    fields = (
        'name', 'description', 'posts'
    )