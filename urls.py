from django.conf.urls.defaults import patterns, url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'baseball.views.home', name='home'),
    # url(r'^baseball/', include('baseball.foo.urls')),

    url(r'draft/import/bbhq/importfinished', 'draft.views.import.bbhq.importFinished'),
    url(r'draft/import/bbhq', 'draft.views.import.bbhq.index'),
    url(r'draft/import/pecota/importfinished', 'draft.views.import.pecota.importFinished'),
    url(r'draft/import/pecota', 'draft.views.import.pecota.index'),

    url(r'draft/batters/changeFilter', 'draft.views.batters.changeFilter'),
    url(r'draft/pitchers/changeFilter', 'draft.views.pitchers.changeFilter'),

    url(r'draft/cleared', 'draft.views.utils.cleared'),
    url(r'draft/clear/pecota', 'draft.views.utils.clearPecota'),
    url(r'draft/clear/bbhq', 'draft.views.utils.clearBbhq'),

    url(r'draft/pick/(?P<player>\d*)/(?P<team>\d*)/(?P<league>\d*)', 'draft.views.pick.add'),
    url(r'draft/thrStarterEdit/(?P<team>\w*)', 'draft.views.import.thrStarter.edit'),
    url(r'draft/showTeams', 'draft.views.import.thrStarter.showTeams'),
    # url(r'draft/show/(?P<league>\d*)'), 'draft.views.pick.show',

    url(r'league/set/(?P<leagueId>\d*)', 'draft.views.utils.setLeague'),

    url(r'projection/set/(?P<projectionType>\w*)', 'draft.views.utils.setProjection'),

    url(r'league/create', 'draft.views.league.create'),
    url(r'league/addTeams/(?P<leagueType>scoresheet|yahoo)/(?P<name>\w*)/(?P<numTeams>\d*)', 'draft.views.league.addTeams'),
    url(r'league/setTeams/(?P<leagueId>\d*)/(?P<numTeams>\d*)', 'draft.views.league.setTeams'),

    url(r'batters/find/(?P<pos>\w{1,3})/(?P<league>AL|NL|MLB)/(?P<orderby>\w*)/(?P<sortorder>ASC|DESC)/(?P<page>\d*)/(?P<showdrafted>0|1)',
        'draft.views.batters.show'),
    url(r'pitchers/find/(?P<pos>SP|RP|ALL)/(?P<league>AL|NL|MLB)/(?P<orderby>\w*)/(?P<sortorder>ASC|DESC)/(?P<page>\d*)/(?P<showdrafted>0|1)',
        'draft.views.pitchers.show'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'draft', 'draft.views.main.show')
)

urlpatterns += staticfiles_urlpatterns()
