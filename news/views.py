#coding=utf-8
from django.views.generic import ListView, DetailView, YearArchiveView, MonthArchiveView, DayArchiveView
from news.models import News
from menus.utils import set_language_changer


class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    paginate_by = 5


class NewsCategoryView(ListView):
    model = News
    template_name = 'news/news_list.html'
    paginate_by = 5

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return News.published.filter(category=category_id)


class NewsItemView(DetailView):
    model = News
    template_name = 'news/news_item.html'


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