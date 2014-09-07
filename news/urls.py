# coding=utf-8
from django.conf.urls import patterns, url
from news.views import NewsListView, NewsCategoryView, NewsYearArchiveView, NewsMonthArchiveView, NewsDayArchiveView, NewsItemView

urlpatterns = patterns('news',
   url(r'^$', NewsListView.as_view(), name='news_index'),
   url(r'^category/(?P<category_id>\d+)/$', NewsCategoryView.as_view(), name='news_archive_year'),
   url(r'^(?P<year>\d{4})/$', NewsYearArchiveView.as_view(), name='news_archive_year'),
   url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', NewsMonthArchiveView.as_view(), name='news_archive_month'),
   url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', NewsDayArchiveView.as_view(), name='news_archive_day'),
   url(r'^(?P<pk>\d+)-(?P<day>\d{2})(?P<month>\d{2})(?P<year>\d{4})/$', NewsItemView.as_view(), name='news_item'),
)
