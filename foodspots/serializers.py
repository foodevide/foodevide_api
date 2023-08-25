# serializers.py
from rest_framework import serializers
from .models import FoodSpot

class FoodSpotSerializer(serializers.ModelSerializer):
    distance_km = serializers.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        model = FoodSpot
        fields = ('id', 'name', 'image', 'rating', 'time', 'location', 'categories', 'reel', 'distance_km')
