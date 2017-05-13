from rest_framework import serializers

from .models import Entity,Period,Department,Role


class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ('id','name','phone','email','dob','department','role','subject')

class EntityAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ('name','phone','email','dob','department','role','subject')


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ('id','entity','room','batch','category','day','start','end')

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id','name','info')

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id','name')