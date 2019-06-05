from rest_framework import serializers
from .models import Dog, DogToy

class DogToySerializer(serializers.ModelSerializer):
    class Meta:
        model = DogToy
        fields = ('id', 'name', 'color')

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ('id', 'name', 'desc', 'age', 'user', 'dog_toys')
