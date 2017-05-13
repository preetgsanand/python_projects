from django.shortcuts import render,get_object_or_404
from .models import Administrator,Supervisor,Employee
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser



from .serializers import AdministratorSerializer,SupervisorSerializer,EmployeeSerializer