# coding=utf-8
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

@apphook_pool.register
class NewsApp(CMSApp):
    name = _("News App")
    urls = ["news.urls"]
    app_name = 'news'
