from django.conf.urls import patterns, include, url

urlpatterns = patterns('cafe.views',    
    url(r'^$', 'home', name='cafe_home'),
)
