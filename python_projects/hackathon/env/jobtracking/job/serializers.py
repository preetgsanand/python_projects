from rest_framework import serializers

from .models import Job,User,Part,Report


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id','name','user','description','deadline','added','status','submitrequest','userRequired','department')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name','phone','email','dob','department','role')

class JobAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('name','userRequired','description','deadline','status','submitrequest','department','user')
    def validate(self, data):
        userRequired = data['userRequired']
        users = User.objects.filter(role=2).order_by('job_count')
        if len(users) >= userRequired:
            users = users[:userRequired]
        for user in users:
            user.job_count += 1
            user.save()
        data['user'] = users
        return data

class UserAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name','phone','email','dob','department','role')

class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ('id','name','job','index')

class PartAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ('name','job','index')

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('id','title','subject','sender','reciever','added','reportType','content')

class ReportAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('title','subject','sender','reciever','added','reportType')