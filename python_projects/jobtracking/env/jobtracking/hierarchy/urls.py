from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
	url(r'^job/list/$',views.JobList.as_view()),
	url(r'^employee/list/$',views.EmployeeList.as_view()),
    url(r'^job/(?P<pk>\d+)/$',views.JobDetail.as_view()),
    url(r'^employee/(?P<pk>\d+)/$',views.EmployeeDetail.as_view()),
    url(r'^entity/list/$',views.EntityList.as_view()),
    url(r'^entity/(?P<pk>\d+)/$',views.EntityDetail.as_view()),
    url(r'^report/list/$',views.ReportList.as_view()),
    url(r'^report/(?P<pk>\d+)/$',views.ReportDetail.as_view()),
    url(r'^job/abandoned/$',views.AbandonedReport.as_view()),
    url(r'^entity/search/$',views.AbandonedReport.as_view()),
]
