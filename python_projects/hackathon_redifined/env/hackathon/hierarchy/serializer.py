from rest_framework import serializers

from .models import Administrator,Supervisor,Employee

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

