from django.urls import path
from . import views

urlpatterns = [
    path('sjh_app/', views.map_main, name='map_main'),
    path('display_map/', views.display_map, name='display_map'),
    path('map_detail/', views.map_detail, name='map_detail'),
    path('map/<str:region>/', views.my_map_detail, name='my_map_detail'),

]
