from geopy.distance import geodesic
from rest_framework import generics
from .models import FoodSpot
from .serializers import FoodSpotSerializer,FoodSpotDetailsSerializer

class FoodSpotList(generics.ListAPIView):
    serializer_class = FoodSpotSerializer
    def get_queryset(self):
        user_latitude = float(self.request.query_params.get('latitude'))
        user_longitude = float(self.request.query_params.get('longitude'))
        user_location = (user_latitude, user_longitude)
        all_food_spots = FoodSpot.objects.all()
        food_spots_with_distance = []
        for food_spot in all_food_spots:
            spot_location = tuple(map(float, food_spot.location.split(',')))
            distance = geodesic(user_location, spot_location).kilometers
            # if distance <= 30:
            food_spots_with_distance.append({
                'id': food_spot.id,
                'name': food_spot.name,
                'image': food_spot.image,
                'rating': food_spot.rating,
                'time': food_spot.time,
                'location': food_spot.location,
                'categories': food_spot.categories.all(),
                'reel': food_spot.reel,
                'distance_km': distance
            })
        sorted_food_spots = sorted(food_spots_with_distance, key=lambda x: x['distance_km'])
        top_30_food_spots = sorted_food_spots[:30]

        return top_30_food_spots

class FoodSpotDetail(generics.RetrieveAPIView):
    serializer_class = FoodSpotDetailsSerializer
    queryset = FoodSpot.objects.all()
    lookup_field = 'id'
