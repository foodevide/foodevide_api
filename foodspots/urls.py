from django.urls import path
from .views import FoodSpotList,FoodSpotDetail

urlpatterns = [
    path('', FoodSpotList.as_view(), name='foodspot-list'),
    path('foodspots/<int:id>', FoodSpotDetail.as_view(), name='foodspot-detail'),

]
