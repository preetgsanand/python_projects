from django.shortcuts import render,get_object_or_404
from .models import Entity,Period,Role,Department,Room,Block,Batch,Subject
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .serializers import PeriodSerializer,EntitySerializer,EntityAddSerializer,DepartmentSerializer,RoleSerializer\
,RoomSerializer,BatchSerializer,BlockSerializer,SubjectSerializer


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

class SubjectList(APIView):

	def get(self,request,format=None):
		snippet = Subject.objects.all()
		serializer = SubjectSerializer(snippet, many=True)
		return Response(serializer.data)


class EntitySearch(APIView):
	def get(self, request, format=None):
		phone = request.GET.get('phone')
		snippet = Entity.objects.filter(phone__contains=phone)
		serializer = EntitySerializer(snippet,many=True)
		if len(snippet) == 0:
			return Response(status=status.HTTP_400_BAD_REQUEST)
		roles = Role.objects.all()
		periods = Period.objects.filter(entity__phone__contains=phone)
		departments = Department.objects.all()
		rooms = Room.objects.all()
		blocks = Block.objects.all()
		batches = Batch.objects.all()
		subjects = Subject.objects.all()

		roleSerializer = RoleSerializer(roles,many=True)
		periodSerializer = PeriodSerializer(periods,many=True)
		departmentSerializer = DepartmentSerializer(departments,many=True)
		roomSerializer = RoomSerializer(rooms,many=True)
		blockSerializer = BlockSerializer(blocks,many=True)
		batchSerializer = BatchSerializer(batches,many=True)
		subjectSerializer = SubjectSerializer(subjects,many=True)

		serialized = []
		serialized.append(serializer.data)
		serialized.append(roleSerializer.data)
		serialized.append(periodSerializer.data)
		serialized.append(departmentSerializer.data)
		serialized.append(roomSerializer.data)
		serialized.append(blockSerializer.data)
		serialized.append(batchSerializer.data)
		serialized.append(subjectSerializer.data)
		return Response(serialized)

class EntityAdd(APIView):
	def put(self,request,format=None):
	    serializer = EntityAddSerializer(data=request.data)
	    if serializer.is_valid():
	    	serializer.save()
	    	return Response(serializer.data)
	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class All(APIView):
	def get(self, request, format=None):
		entities = Entity.objects.all()
		roles = Role.objects.all()
		periods = Period.objects.all()
		departments = Department.objects.all()
		rooms = Room.objects.all()
		blocks = Block.objects.all()
		batches = Batch.objects.all()
		subjects = Subject.objects.all()

		entitySerializer = EntitySerializer(entities,many=True)
		roleSerializer = RoleSerializer(roles,many=True)
		periodSerializer = PeriodSerializer(periods,many=True)
		departmentSerializer = DepartmentSerializer(departments,many=True)
		roomSerializer = RoomSerializer(rooms,many=True)
		blockSerializer = BlockSerializer(blocks,many=True)
		batchSerializer = BatchSerializer(batches,many=True)
		subjectSerializer = SubjectSerializer(subjects,many=True)

		serialized = []
		serialized.append(entitySerializer.data)
		serialized.append(roleSerializer.data)
		serialized.append(periodSerializer.data)
		serialized.append(departmentSerializer.data)
		serialized.append(roomSerializer.data)
		serialized.append(blockSerializer.data)
		serialized.append(batchSerializer.data)
		serialized.append(subjectSerializer.data)
		return Response(serialized)