
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),   
    path('users/', include("users_app.urls")), 
    path('', include("inneats_app.urls")), 
    
    # accommodation_app 추가 - kyj
    path('', include("accommodation_app.urls")),  

    # kdy_app 추가 - kdy
    path('', include("kdy_app.urls")),
    # search 추가 - hst
    path('', include("search.urls")),

    path('', include("attraction_app.urls")),
    # sjh_app 추가 - sjh
    path('', include("sjh_app.urls")),
]
