from rest_framework import serializers

from .models import Entity,Period,Role,Department,Room,Block,Batch,Subject


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
        fields = ('id','entity','room','batch','category','weekday','start','end','subject')

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id','name','info')

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id','name')

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id','name','block','floor','category','assisstant')

class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ('id','name')

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = ('id','department','year','shift')

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id','code','name')