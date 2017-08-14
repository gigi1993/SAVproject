from django.conf.urls import url
from . import views

urlpatterns = [
#    url(r'^$', views.home, name='home'),
#    url(r'^participate$', views.participate, name='participate'),
    url(r'^$', views.overview, name='overview'),
    url(r'^about$', views.about, name='about'),
    url(r'^previewNL$', views.previewNL, name='previewNL'),
    url(r'^previewUK$', views.previewUK, name='previewUK'),
    url(r'^UK$', views.UK, name='UK'),
]