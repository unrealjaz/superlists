from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'lists.views.home_page', name='home'),
    url(r'^lists/the-only-list-in-the-world/$', 'lists.views.view_list', name='view_list'),
)
