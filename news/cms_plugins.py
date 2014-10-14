# coding=utf-8
from unicodedata import category
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

    def get_render_template(self, context, instance, placeholder):
        return 'news/{}.html'.format(instance.template_name)

    def render(self, context, instance, placeholder):
        """
            Render the latest entries
        """
        qs = News.published.all()
        if instance.category is not True:
            qs = qs.filter(category=instance.category)

        latest = qs[:instance.limit]

        context.update({
            'instance': instance,
            'latest': latest,
            'object_list': latest,
            'placeholder': placeholder,
        })
        return context
