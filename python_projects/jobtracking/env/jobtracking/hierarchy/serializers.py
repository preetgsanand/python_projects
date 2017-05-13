from rest_framework import serializers

from .models import Administrator,Supervisor,Employee,Job,Entity,Report


class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ('id','name','email','dob','added')

class AdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = ('id','name','email','dob','added')

class SupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supervisor
        fields = ('id','name','email','dob','added')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id','name','email','dob','added')


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('id','heading','content','date','sender','reciever','reportType')

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id','name','added','deadline','jobemployee','userRequired','description','department','status','skills','difficulty','submitrequest')