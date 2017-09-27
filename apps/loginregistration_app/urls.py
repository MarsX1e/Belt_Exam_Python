from django.conf.urls import url
from django.contrib import admin
from . import views
def test(request):
    print 'jofiajeijefp'
urlpatterns = [
    url(r'^$',views.go),
    url(r'^main/$',views.index),
    url(r'^registrationprocess/$',views.registration),
    url(r'^loginprocess/$',views.login),
    url(r'^logout/$',views.loginout),
]
