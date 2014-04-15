from django.conf.urls import patterns, include, url

urlpatterns = patterns('linkbase.views',    
    url(r'^vouchers/$', 'vouchers', name='vouchers'),
)
