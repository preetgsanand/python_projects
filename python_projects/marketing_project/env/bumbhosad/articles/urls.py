
from django.conf.urls import url,include
from . import views
urlpatterns = [
	url(r'^$', views.index),
    url(r'health/$', views.health),
    url(r'contact_us/$', views.contact),
    url(r'entertainment/$', views.entertainment),
    url(r'finance/$', views.finance),
    url(r'loans/$', views.loans),
    url(r'politics/$', views.politics),
    url(r'^list/(?P<id>\d+)/$',views.detail,name="detail"),
]