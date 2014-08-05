# coding=utf-8 
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from news.models import LatestNewsPlugin, News


@plugin_pool.register_plugin
class CMSLatestNewsPlugin(CMSPluginBase):
    """
        Plugin class for the latest news
    """
    model = LatestNewsPlugin
    name = _('Latest news')
    render_template = "news/latest_news.html"

    def render(self, context, instance, placeholder):
        """
            Render the latest entries
        """
        qs = News.published.all()

        latest = qs[:instance.limit]

        context.update({
            'instance': instance,
            'latest': latest,
            'object_list': latest,
            'placeholder': placeholder,
        })
        return context