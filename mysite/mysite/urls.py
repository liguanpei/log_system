import mysite
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^device_info/(?P<area_name>.*)$', 'mysite.views.device_info', {'template_name': 'device_info.html'}, name='device_info'),
    url(r'^device_create', 'mysite.views.device_create', {'template_name': 'device_create.html'}, name='device_create'),
    url(r'^area_info/$', 'mysite.views.area_info', {'template_name': 'area_info.html'}, name='area_info'),
    url(r'^area_create', 'mysite.views.area_create', {'template_name': 'area_create.html'}, name='area_create'),
    url(r'^email_info/$', 'mysite.views.email_info', {'template_name': 'email_info.html'}, name='email_info'),
    url(r'^person_info/$', 'mysite.views.person_info', {'template_name': 'person_info.html'}, name='person_info'),
    url(r'^email_create', 'mysite.views.email_create', {'template_name': 'email_create.html'}, name='email_create'),
    url(r'^history_log/(?P<dev_name>.*)$', 'mysite.views.history_log', {'template_name': 'history_log.html'}, name='history_log'),
    url(r'^delete/$', 'mysite.views.delete', name='delete'),
)
