from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'totroops.views.beta_signup', name='beta_signup'),
    url(r'thanks/^$', 'totroops.views.thanks', name='thanks'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
