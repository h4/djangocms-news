#coding=utf-8
from django.contrib import admin
from hvad.admin import TranslatableAdmin
from news.models import News, NewsImage, Category


class NewsImageAdmin(admin.StackedInline):
    model = NewsImage
    extra = 0


class NewsAdmin(TranslatableAdmin):
    inlines = [
        NewsImageAdmin
    ]

admin.site.register(News, NewsAdmin)
admin.site.register(Category, TranslatableAdmin)
