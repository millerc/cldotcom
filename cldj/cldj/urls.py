from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cldj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'frontpage.views.home', name='home'),
    url(r'^legal/$', 'frontpage.views.legal', name='legal'),
    url(r'^contact-us/$', 'contactus.views.contact_list', name='contact_list'),
    url(r'^chamber-services/', include('chamberservices.urls')),
    url(r'^cafe/', include('cafe.urls')),
)

