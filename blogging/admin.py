
from django.contrib import admin

from blogging.models import Post, Category, ModelAdmin2


class ModelAdminClass(admin.TabularInline):
    model = ModelAdmin2
    extra = 1


class PostAdmin(admin.ModelAdmin):
    inlines = (ModelAdminClass,)


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)


# and a new admin registration
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
# Register your models here.
