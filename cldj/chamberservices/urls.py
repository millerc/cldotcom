from django.conf.urls import patterns, include, url

urlpatterns = patterns('chamberservices.views',    
    url(r'^request-quote/$', 'request_proposal', name='request_proposal'),
    url(r'^(?P<slug>[\w-]+)/$', 'default', name='cs_default'),
    url(r'^$', 'default', {'slug': 'tell-your-story'}, name='cs_root'),    
)
