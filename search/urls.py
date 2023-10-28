from django.urls import path
from. import views

urlpatterns = [
    path('search/<str:property_type>/<str:location>/<str:search_input>/', views.search, name='search'),
]
