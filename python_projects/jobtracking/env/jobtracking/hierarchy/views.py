from django.shortcuts import render,get_object_or_404
from .models import Administrator,Supervisor,Employee,Job,Entity,Report
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser



from .serializers import AdministratorSerializer,SupervisorSerializer,EmployeeSerializer,JobSerializer,EntitySerializer,ReportSerializer


class JobList(APIView):

	def get(self,request,format=None):
		jobs = Job.objects.all()
		serializer = JobSerializer(jobs, many=True)
		return Response(serializer.data)

class JobDetail(APIView):
	def get_object(self, pk):
		try:
			return Job.objects.get(pk=pk)
		except Job.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		snippet = self.get_object(pk)
		serializer = JobSerializer(snippet)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
	    job = self.get_object(pk)
	    serializer = JobSerializer(job, data=request.data)
	    if serializer.is_valid():
	    	serializer.save()
	    	return Response(serializer.data)
	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeList(APIView):

	def get(self,request,format=None):
		employees = Employee.objects.all()
		serializer = EmployeeSerializer(employees, many=True)
		return Response(serializer.data)

class EmployeeDetail(APIView):
	def get_object(self, pk):
		try:
			return Employee.objects.get(pk=pk)
		except Employee.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		snippet = self.get_object(pk)
		serializer = EmployeeSerializer(snippet)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
	    employee = self.get_object(pk)
	    serializer = EmployeeSerializer(employee, data=request.data)
	    if serializer.is_valid():
	    	serializer.save()
	    	return Response(serializer.data)
	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EntityList(APIView):

	def get(self,request,format=None):
		entities = Entity.objects.all()
		serializer = EntitySerializer(entities, many=True)
		return Response(serializer.data)

class EntityDetail(APIView):
	def get_object(self, pk):
		try:
			return Entity.objects.get(pk=pk)
		except Entity.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		snippet = self.get_object(pk)
		serializer = EntitySerializer(snippet)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
	    entity = self.get_object(pk)
	    serializer = EntitySerializer(entity, data=request.data)
	    if serializer.is_valid():
	    	serializer.save()
	    	return Response(serializer.data)
	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReportList(APIView):

	def get(self,request,format=None):
		entities = Report.objects.all()
		serializer = ReportSerializer(entities, many=True)
		return Response(serializer.data)

class ReportDetail(APIView):
	def get_object(self, pk):
		try:
			return Report.objects.get(pk=pk)
		except Report.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		snippet = self.get_object(pk)
		serializer = ReportSerializer(snippet)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
	    report = self.get_object(pk)
	    serializer = ReportSerializer(report, data=request.data)
	    if serializer.is_valid():
	    	serializer.save()
	    	return Response(serializer.data)
	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AbandonedReport(APIView):
	def put(self,request,format=None):
		serializer = JobSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		jobid = request.GET.get('jobid')
		empid = request.GET.get('empid')
		employee = Employee.objects.get(pk=empid)
		job = Job.objects.get(pk=jobid)
		supervisor = employee.employeeSupervisor
		report = Report(heading="Job Available",content="Job "+job.name+" Available",sender=supervisor,reportType=1)
		report.save()
	
	def get_object(self, pk):
		try:
			return Job.objects.get(pk=pk)
		except Job.DoesNotExist:
			raise Http404

class EntitySearch(APIView):
	def get(self,request,format=None):
		phone = request.GET.get('phone')
		entities = Entity.objects.filter(phone__contains=phone)
		serializer = EntitySerializer(data=entities)
		return Response(serializer.data)
