from django.conf.urls import url,include
from . import views


urlpatterns = [
	url(r'^$', views.index),
	url(r'^floor_maintenance/$', views.floor_maintenance),
	url(r'^densification/$', views.densification),
	url(r'^floor_solutions/$', views.floor_solutions),
	url(r'^floor_preparations/$', views.floor_preparations),
	url(r'^contact_us/$', views.contact_us),
]