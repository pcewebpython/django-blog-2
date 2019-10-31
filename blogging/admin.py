from django.contrib import admin

from blogging.models import Post, Category

# and a new admin registration
admin.site.register(Post)
admin.site.register(Category)
# Register your models here.
