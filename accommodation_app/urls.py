
from django.urls import path
from . import views

urlpatterns = [
    path('accommodation/<str:keyword>', views.accommodation, name='accommodation'),
    path('accommodation_detail/<str:accommodation_id>', views.accommodation_detail, name='accommodation_detail'),
]
