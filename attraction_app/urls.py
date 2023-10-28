from django.urls import path
from . import views
urlpatterns = [
    path('attraction/<str:keyword>', views.attraction, name='attraction'),
    path('attraction_detail/<str:pk>', views.attraction_detail, name='attraction_detail'),
]

