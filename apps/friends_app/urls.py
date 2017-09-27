from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^friends/$',views.friends),
    url(r'^friends/(?P<id>\d+)/remove/$',views.remove),
    url(r'^friends/add/(?P<id>\d+)/$',views.add),
    url(r'^user/(?P<id>\d+)/$',views.user),
]
