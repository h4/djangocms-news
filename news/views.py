#coding=utf-8
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, YearArchiveView, MonthArchiveView, DayArchiveView
from django.utils.translation import ugettext_lazy as _
from news.models import News
from menus.utils import set_language_changer


class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    paginate_by = 5


class NewsItemView(DetailView):
    model = News
    template_name = 'news/news_item.html'

    # def get(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     menu = request.toolbar.get_or_create_menu('news-app', _('News'))
    #     menu.add_break()
    #     url = reverse('admin:news_news_change', args=[self.object.pk,])
    #     menu.add_modal_item(_('Edit this news'), url=url)
    #     url = reverse('admin:news_news_delete', args=[self.object.pk,])
    #     menu.add_modal_item(_('Delete this news'), url=url)
    #     context = self.get_context_data(object=self.object)
    #     return self.render_to_response(context)


class NewsArchiveMixin(object):
    model = News
    date_field = 'pub_date'
    make_object_list = True
    allow_empty = True
    month_format = "%m"

    def get_queryset(self):
        queryset = super(NewsArchiveMixin, self).published
        if queryset:
            set_language_changer(self.request, queryset[0].language_changer)
        return queryset


class NewsYearArchiveView(NewsArchiveMixin, YearArchiveView):
    template_name = 'news/news_archive_year.html'


class NewsMonthArchiveView(NewsArchiveMixin, MonthArchiveView):
    template_name = 'news/news_archive_month.html'


class NewsDayArchiveView(NewsArchiveMixin, DayArchiveView):
    template_name = 'news/news_archive_day.html'