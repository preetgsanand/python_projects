from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name','phone','email','address','facebook','instagram','added')

class UserAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name','phone','email','address','facebook','instagram','added')