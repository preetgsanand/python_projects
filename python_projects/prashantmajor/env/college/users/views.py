from django.shortcuts import render,get_object_or_404
from .models import Entity,Period,Role,Department
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser



from .serializers import PeriodSerializer,EntitySerializer,EntityAddSerializer,DepartmentSerializer,RoleSerializer


class EntityList(APIView):

	def get(self,request,format=None):
		snippet = Entity.objects.all()
		serializer = EntitySerializer(snippet, many=True)
		return Response(serializer.data)

class DepartmentList(APIView):

	def get(self,request,format=None):
		snippet = Department.objects.all()
		serializer = DepartmentSerializer(snippet, many=True)
		return Response(serializer.data)

class RoleList(APIView):

	def get(self,request,format=None):
		snippet = Role.objects.all()
		serializer = RoleSerializer(snippet, many=True)
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
	    snippet = self.get_object(pk)
	    serializer = EntitySerializer(snippet, data=request.data)
	    if serializer.is_valid():
	    	serializer.save()
	    	return Response(serializer.data)
	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PeriodList(APIView):

	def get(self,request,format=None):
		snippet = Period.objects.all()
		serializer = PeriodSerializer(snippet, many=True)
		return Response(serializer.data)

class PeriodDetail(APIView):
	def get_object(self, pk):
		try:
			return Period.objects.get(pk=pk)
		except Period.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		snippet = self.get_object(pk)
		serializer = PeriodSerializer(snippet)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
	    snippet = self.get_object(pk)
	    serializer = PeriodSerializer(snippet, data=request.data)
	    if serializer.is_valid():
	    	serializer.save()
	    	return Response(serializer.data)
	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PeriodSearch(APIView):
	def get(self, request, format=None):
		phone = request.GET.get('phone')
		snippet = Period.objects.filter(entity__phone__contains=phone)
		serializer = PeriodSerializer(snippet,many=True)
		return Response(serializer.data)

class EntitySearch(APIView):
	def get(self, request, format=None):
		phone = request.GET.get('phone')
		snippet = Entity.objects.filter(phone__contains=phone)
		serializer = EntitySerializer(snippet,many=True)
		return Response(serializer.data)

class EntityAdd(APIView):
	def put(self,request,format=None):
	    serializer = EntityAddSerializer(data=request.data)
	    if serializer.is_valid():
	    	serializer.save()
	    	return Response(serializer.data)
	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)