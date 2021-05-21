from django.contrib import admin
from .models import Post, Comment
from blog import models
# Register your models here.
class CommentInLine(admin.StackedInline):
    model = Comment
    list_display = ['author', 'body', 'date']
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['date']
    search_fields = ['id', 'title']
    inlines = [CommentInLine]
admin.site.register(Post, PostAdmin)