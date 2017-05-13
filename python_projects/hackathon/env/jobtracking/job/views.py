from django.shortcuts import render,get_object_or_404
from .models import User,Report,Part,Job
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser



from .serializers import JobSerializer,UserSerializer,JobAddSerializer,UserAddSerializer,PartSerializer,PartAddSerializer\
,ReportSerializer,ReportAddSerializer


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
	    serializer = UserSerializer(user, data=request.data)
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
		phone = request.GET.get('phone')
		users = User.objects.filter(phone__contains=phone)
		serializer = UserSerializer(users,many=True)
		return Response(serializer.data)

class ReportList(APIView):

	def get(self,request,format=None):
		reports = Report.objects.all()
		serializer = ReportSerializer(reports, many=True)
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


class JobSearch(APIView):
	def get(self, request, format=None):
		phone = request.GET.get('phone')
		name = request.GET.get('name')
		if phone != None and name != None:
			jobs = Job.objects.filter(user__phone__contains=phone,name__contains=name)
		elif phone != None:
			jobs = Job.objects.filter(user__phone__contains=phone)
		elif name != None:
			jobs = Job.objects.filter(name__contains=name)
		else:
			return Response(status=status.HTTP_204_NO_CONTENT)
			
		serializer = JobSerializer(jobs,many=True)
		return Response(serializer.data)

class PartSearch(APIView):
	def get(self, request, format=None):
		id = request.GET.get('id')
		if id != None:
			parts = Part.objects.filter(job=	id)
			serializer = PartSerializer(parts,many=True)
			return Response(serializer.data)
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)

class PartList(APIView):

	def get(self,request,format=None):
		parts = Part.objects.all()
		serializer = PartSerializer(parts, many=True)
		return Response(serializer.data)

class UserAdd(APIView):
	def put(self,request,format=None):
	    serializer = UserAddSerializer(data=request.data)
	    if serializer.is_valid():
	    	serializer.save()
	    	return Response(serializer.data)
	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobAdd(APIView):
	def put(self,request,format=None):
	    serializer = JobAddSerializer(data=request.data)
	    if serializer.is_valid():
	    	userRequired = serializer.validated_data['userRequired']
	    	department = serializer.validated_data['department'] 
	    	users = User.objects.filter(role=2).order_by('job_count')
	    	if len(users) >= userRequired:
	    		users = users[:userRequired]
	    	for user in users:
	    		user.job_count += 1
	    		user.save()
	    	serializer.save()
	    	return Response(serializer.data)
	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReportAdd(APIView):
	def put(self,request,format=None):
	    serializer = ReportAddSerializer(data=request.data)
	    if serializer.is_valid():
	    	serializer.save()
	    	return Response(serializer.data)
	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReportSearch(APIView):
	def get(self, request, format=None):
		sender = request.GET.get('sender')
		reciever = request.GET.get('reciever')
		if sender != None and reciever != None:
			reports = Report.objects.filter(sender=sender,reciever=reciever)
		elif sender != None:
			reports = Report.objects.filter(sender=sender)
		elif reciever != None:
			reports = Report.objects.filter(reciever=reciever)
		serializer = ReportSerializer(reports,many=True)
		return Response(serializer.data)

def index(request):
	context = {

	}
	return render(request,'index.html',context)
