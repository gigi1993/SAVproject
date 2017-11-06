from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.overview, name='overview'),
    url(r'^about$', views.about, name='about'),
    url(r'^details_AS_UK$', views.details_AS_UK, name='details_AS_UK'),
    url(r'^details_AS_DE$', views.details_AS_DE, name='details_AS_DE'),
    url(r'^details_TAB_UK$', views.details_TAB_UK, name='details_TAB_UK'),
    url(r'^details_TAB_DE$', views.details_TAB_DE, name='details_TAB_NL'),
#    url(r'^$', views.home, name='home'),
#    url(r'^participate$', views.participate, name='participate'),
#    url(r'^previewNL$', views.previewNL, name='previewNL'),
#    url(r'^previewUK$', views.previewUK, name='previewUK'),
#    url(r'^UK$', views.UK, name='UK'),
]
