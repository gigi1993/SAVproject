from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^participate$', views.participate, name='participate'),
    url(r'^overview$', views.overview, name='overview'),
    url(r'^myfirstout$', views.myfirstout, name='myfirstout'),
    url(r'^line$', views.line, name='line'),
]