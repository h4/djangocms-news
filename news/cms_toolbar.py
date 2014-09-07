# coding=utf-8 
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar


@toolbar_pool.register
class NewsToolbar(CMSToolbar):
    def populate(self):
        if self.is_current_app:
            menu = self.toolbar.get_or_create_menu('news-app', _('News'), position=1)
            url = reverse('admin:news_news_add')
            menu.add_modal_item(_('Add news'), url=url)
