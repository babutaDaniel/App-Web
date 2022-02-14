from django.contrib import admin
from . models import Product, Comment


class ProductAdmin(admin.ModelAdmin):
    fields =['name', 'type', 'description', ('profile_image', 'second_image', 'third_image'), 'rating', 'is_published', 'created_at']
    list_display = ('id', 'name', 'rating', 'is_published', 'created_at')
    list_display_links = ('id', 'name')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'timestamp')
    list_display_links = ('post', 'user')

    list_filter = ('user', 'post', 'timestamp')


admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)



