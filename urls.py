from django.conf.urls.defaults import patterns, url, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'baseball.views.home', name='home'),
    # url(r'^baseball/', include('baseball.foo.urls')),
    url(r'draft/import/pecota/importfinished', 'draft.views.import.pecota.importFinished'),
    url(r'draft/import/pecota/', 'draft.views.import.pecota.index'),

    url(r'draft/clear/', 'draft.views.utils.clear'),
    url(r'draft/cleared/', 'draft.views.utils.cleared'),
    url(r'draft/pick/?P<player>\d*/?P<team>\d*/?P<league>\d*', 'draft.views.pick.add'),

    url(r'league/create', 'draft.views.league.create'),
    url(r'league/addTeams/(?P<leagueType>scoresheet|yahoo)/(?P<name>\w*)/(?P<numTeams>\d*)', 'draft.views.league.addTeams'),
    url(r'league/setTeams/(?P<leagueId>\d*)/(?P<numTeams>\d*)', 'draft.views.league.setTeams'),

    url(r'batters/find/(?P<pos>\w{1,3})/(?P<league>AL|NL|MLB)/(?P<orderby>\w*)/(?P<sortorder>ASC|DESC)',
        'draft.views.batters.show'),
    url(r'pitchers/find/(?P<pos>SP|RP|ALL)/(?P<league>AL|NL|MLB)/(?P<orderby>\w*)/(?P<sortorder>ASC|DESC)',
        'draft.views.pitchers.show'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls))
)
