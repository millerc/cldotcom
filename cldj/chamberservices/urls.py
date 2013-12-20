from django.conf.urls import patterns, include, url

urlpatterns = patterns('chamberservices.views',    
    url(r'^request-quote/$', 'request_proposal', name='request_proposal'),
    url(r'^$', 'default', name='cs_default'),
)
