from django.contrib import admin
from blog.models import *


# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'pub_time')


admin.site.register((Category, Comment, Tag))
