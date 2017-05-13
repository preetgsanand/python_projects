from django.shortcuts import render,get_object_or_404
from .models import Artist,User
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser



from .serializers import ArtistSerializer,UserSerializer


class ArtistList(APIView):

	def get(self,request,format=None):
		artists = Artist.objects.all()
		serializer = ArtistSerializer(artists, many=True)
		return Response(serializer.data)

class ArtistDetail(APIView):
	def get_object(self, pk):
		try:
			return Artist.objects.get(pk=pk)
		except Artist.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		snippet = self.get_object(pk)
		serializer = ArtistSerializer(snippet)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
	    artist = self.get_object(pk)
	    serializer = ArtistSerializer(artist, data=request.data)
	    if serializer.is_valid():
	    	serializer.save()
	    	return Response(serializer.data)
	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	#def delete(self, request, pk, format=None):
	#	artist = self.get_object(pk)
	#	artist.delete()
	#	return Response(status=status.HTTP_204_NO_CONTENT)

class UserList(APIView):

	def get(self,request,format=None):
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)

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
	    serializer = ArtistSerializer(user, data=request.data)
	    if serializer.is_valid():
	    	serializer.save()
	    	return Response(serializer.data)
	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		user = self.get_object(pk)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class UserSearch(APIView):
	def get(self, request, format=None):
		name = request.GET.get('name')
		users = User.objects.filter(name__contains=name)
		serializer = UserSerializer(users,many=True)
		return Response(serializer.data)


class ArtistSearch(APIView):
	def get(self, request, format=None):
		name = request.GET.get('name')
		artists = Artist.objects.filter(name__contains=name)
		serializer = ArtistSerializer(artists,many=True)
		return Response(serializer.data)


class UserAdd(APIView):
	def put(self,request,format=None):
	    serializer = UserSerializer(data=request.data)
	    if serializer.is_valid():
	    	serializer.save()
	    	return Response(serializer.data)
	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def index(request):
	context = {

	}
	return render(request,'index.html',context)
