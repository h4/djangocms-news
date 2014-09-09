#coding=utf-8
from django.contrib import admin
from hvad.admin import TranslatableAdmin
from news.models import News, NewsImage, Category
from genericadmin.admin import GenericAdminModelAdmin, StackedInlineWithGeneric


class NewsImageAdmin(StackedInlineWithGeneric):
    model = NewsImage
    extra = 0


class NewsAdmin(GenericAdminModelAdmin, TranslatableAdmin):
    inlines = [
        NewsImageAdmin
    ]

admin.site.register(News, NewsAdmin)
admin.site.register(Category, TranslatableAdmin)
