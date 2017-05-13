from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
	url(r'^$',views.index	),
	url(r'^artist/list/$',views.ArtistList.as_view()),
	url(r'^user/list/$',views.UserList.as_view()),
    #url(r'^list/(?P<id>\d+)/$',views.detail,name="detail"),
    url(r'^user/(?P<pk>\d+)/$',views.UserDetail.as_view()),
    url(r'^artist/(?P<pk>\d+)/$',views.ArtistDetail.as_view()),
    url(r'^user/search/$',views.UserSearch.as_view()),
    url(r'^artist/search/$',views.ArtistSearch.as_view()),
    url(r'^user/add/$',views.UserAdd.as_view()),
]