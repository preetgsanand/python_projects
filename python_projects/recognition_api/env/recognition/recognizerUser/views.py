from django.shortcuts import render,get_object_or_404
from .models import User
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser



from .serializers import UserSerializer,UserAddSerializer

class UserDetail(APIView):
	def get_object(self, pk):
		try:
			return User.objects.get(pk=pk)
		except User.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		user = self.get_object(pk)
		serializer = UserSerializer(user)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
	    user = self.get_object(pk)
	    serializer = UserSerializer(user, data=request.data)
	    if serializer.is_valid():
	    	serializer.save()
	    	return Response(serializer.data)
	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		user = self.get_object(pk)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class UserAdd(APIView):
	def put(self,request,format=None):
	    serializer = UserAddSerializer(data=request.data)
	    email = request.GET.get('email')
	    users = User.objects.filter(email__contains=email)
	    if users.count() > 0:
	    	return Response({'status':'100'})
	    if serializer.is_valid():
	    	serializer.save()
	    	return Response(status=status.HTTP_200_OK)
	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserSearch(APIView):
	def get(self, request, format=None):
		name = request.GET.get('name')
		arr = name.split('_')
		users = User.objects.filter(name__contains=" ".join(arr))
		serializer = UserSerializer(users,many=True)
		return Response(serializer.data)

class UserList(APIView):

	def get(self,request,format=None):
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)