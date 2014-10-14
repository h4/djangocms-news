# coding=utf-8
from datetime import datetime
from django.contrib.contenttypes.models import ContentType
from django.db import models
from ckeditor.fields import RichTextField as HTMLField
from filer.fields.image import FilerImageField
from hvad.models import TranslatableModel, TranslatedFields, TranslationManager
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin
from model_utils.models import TimeStampedModel
from django.contrib.contenttypes import generic


class PublishedNewsManager(TranslationManager):
    def get_query_set(self):
        return self.language().filter(is_published=True, pub_date__lte=datetime.now()).order_by('-pub_date')


class News(TranslatableModel, TimeStampedModel):
    translations = TranslatedFields(
        title=models.CharField(_('Title'), max_length=256, null=True, blank=True),
        lead=HTMLField(_('Lead'), null=True, blank=True),
        description=HTMLField(_('Description')),
    )

    content_type = models.ForeignKey(ContentType, verbose_name=_('linked entity'), null=True, blank=True)
    object_id = models.PositiveIntegerField('entity id', null=True, blank=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    category = models.ForeignKey('Category', verbose_name=_('category'), null=True, blank=True)
    is_published = models.BooleanField(_('Is published'))
    pub_date = models.DateTimeField(_('Publication Date'), default=datetime.now)

    published = PublishedNewsManager()

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News_plural')
        ordering = ['-pub_date',]

    @property
    def cover_image(self):
        if len(self.images.all()):
            return self.images.all()[0].image

    def __unicode__(self):
        return self.safe_translation_getter('title', _('News at: %s' % self.pub_date))

    @models.permalink
    def get_absolute_url(self):
        return ('news_item', (), {
            'year': self.pub_date.year,
            'month': self.pub_date.month,
            'day': self.pub_date.day,
            'pk': self.pk
        })

    def language_changer(self, language):
        return self.get_absolute_url()


class NewsImage(TimeStampedModel):
    news = models.ForeignKey(News, related_name='images')
    image = FilerImageField(verbose_name=_('Image'), blank=True, null=True)

    def __unicode__(self):
        return self.news.__unicode__()


class Category(TranslatableModel, TimeStampedModel):
    translations = TranslatedFields(
        title=models.CharField(_('Title'), max_length=256, null=True, blank=True),
    )

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __unicode__(self):
        return self.lazy_translation_getter('title', _('Category %s' % self.pk))


class LatestNewsPlugin(CMSPlugin):
    """
        Model for the settings when using the latest news cms plugin
    """
    category = models.ForeignKey(Category, verbose_name=_('category'), null=True, blank=True)
    limit = models.PositiveIntegerField(_('Number of news to show'),
                                        help_text=_('Limits the number of news that will be displayed'))
    show_cover = models.BooleanField(_('Show cower'), default=True)
    template_name = models.CharField(_('template name'), max_length=255, default='latest_news')
