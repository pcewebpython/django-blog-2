from django.contrib import admin
from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'title':('text',)}

class CatagoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'name':('description',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CatagoryAdmin)
