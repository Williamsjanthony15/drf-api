from django.urls import path
from .views import VehicleList, VehicleDetail

urlpatterns = [
    path('', VehicleList.as_view(), name='vehicle_list'),
    path('<int:pk>/', VehicleDetail.as_view(), name='vehicle_detail')
]