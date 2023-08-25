from django.urls import path
from .views import FoodSpotList

urlpatterns = [
    path('', FoodSpotList.as_view(), name='foodspot-list'),

]
