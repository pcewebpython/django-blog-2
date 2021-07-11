from django.contrib import admin

from blogging.models import Post, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

    exclude = ('posts',)

class CategoryInLine(admin.TabularInline):
    model = Category.posts.through

class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInLine,]
    
    list_display = ('title', 'created_date',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)