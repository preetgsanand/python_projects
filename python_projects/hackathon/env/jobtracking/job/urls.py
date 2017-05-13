from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
	url(r'^$',views.index),
	url(r'^job/list/$',views.JobList.as_view()),
	url(r'^user/list/$',views.UserList.as_view()),
    url(r'^user/(?P<pk>\d+)/$',views.UserDetail.as_view()),
    url(r'^job/(?P<pk>\d+)/$',views.JobDetail.as_view()),
    url(r'^user/search/$',views.UserSearch.as_view()),
    url(r'^job/search/$',views.JobSearch.as_view()),
    url(r'^user/add/$',views.UserAdd.as_view()),
    url(r'^job/add/$',views.JobAdd.as_view()),
    url(r'^part/search/$',views.PartSearch.as_view()),
    url(r'^part/list/$',views.PartList.as_view()),
    url(r'^report/list/$',views.ReportList.as_view()),
    url(r'^report/(?P<pk>\d+)/$',views.ReportDetail.as_view()),
    url(r'^report/search/$',views.ReportSearch.as_view()),
    url(r'^report/add/$',views.ReportAdd.as_view()),
]