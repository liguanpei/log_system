import mysite
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^index/$', 'mysite.views.index', {'template_name': 'index.html'}, name='index'),
    url(r'^delete/$', 'mysite.views.delete', name='delete'),
    url(r'^device_create', 'mysite.views.device_create', {'template_name': 'device_create.html'}, name='device_create'),
    url(r'^history_log/(?P<dev_name>.*)$', 'mysite.views.history_log', {'template_name': 'history_log.html'}, name='history_log'),
)
