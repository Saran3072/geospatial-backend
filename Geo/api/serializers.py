from rest_framework import serializers
from ..models import geo

class GeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = geo
        fields = ('id', 'image', 'result')