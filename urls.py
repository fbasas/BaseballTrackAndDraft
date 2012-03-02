from django.conf.urls.defaults import patterns, url, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'baseball.views.home', name='home'),
    # url(r'^baseball/', include('baseball.foo.urls')),
    url(r'draft/import/pecota/battersfinished', 'draft.views.import.pecota.battersFinished'),
    url(r'draft/import/pecota/', 'draft.views.import.pecota.index'),

    url(r'draft/clear/', 'draft.views.utils.clear'),
    url(r'draft/cleared/', 'draft.views.utils.cleared'),

    url(r'batters/find/(?P<pos>\w{2})', 'draft.views.batters.show'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls))
)
