from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
	url(r'^user/list/$',views.UserList.as_view()),
    url(r'^user/(?P<pk>\d+)/$',views.UserDetail.as_view()),
    url(r'^user/search/$',views.UserSearch.as_view()),
    url(r'^user/add/$',views.UserAdd.as_view()),
]