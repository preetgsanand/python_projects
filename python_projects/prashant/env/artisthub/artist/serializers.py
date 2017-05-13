from rest_framework import serializers

from .models import Artist,User


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id','name','born','nationality','awards','work',
        	'contact','popularity')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name','phone','email','born')