from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
	url(r'^entity/list/$',views.EntityList.as_view()),
	url(r'^period/list/$',views.PeriodList.as_view()),
    url(r'^role/list/$',views.RoleList.as_view()),
    url(r'^department/list/$',views.DepartmentList.as_view()),
    url(r'^entity/(?P<pk>\d+)/$',views.EntityDetail.as_view()),
    url(r'^period/(?P<pk>\d+)/$',views.PeriodDetail.as_view()),
    url(r'^entity/search/$',views.EntitySearch.as_view()),
    url(r'^period/search/$',views.PeriodSearch.as_view()),
    url(r'^entity/add/$',views.EntityAdd.as_view()),
]