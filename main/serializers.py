# main/serializers.py

from rest_framework import serializers
from .models import City

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'name_en', 'name_tr', 'description', 'description_en', 'description_tr']