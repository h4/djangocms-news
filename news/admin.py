#coding=utf-8
from django.contrib import admin
from hvad.admin import TranslatableAdmin
from news.models import News, NewsImage


class NewsImageAdmin(admin.StackedInline):
    model = NewsImage
    extra = 0


class NewsAdmin(TranslatableAdmin):
    inlines = [
        NewsImageAdmin
    ]

admin.site.register(News, NewsAdmin)
