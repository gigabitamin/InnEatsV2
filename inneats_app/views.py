# from django.http import HttpResponse, JsonResponse
# from django.core import serializers
# import json
# from .models import NaverBlog
# from .models import Youtube
# from django.db.models import Q
# from .forms import YoutubeForm
# from .forms import NaverBlogForm
# from .forms import UserInfoForm
# from .forms import ImageForm
# from .models import UsersAppUser
# from django.views.generic.edit import DeleteView
# from django.contrib.auth.models import User
# from users_app.models import User

from django.shortcuts import get_object_or_404, render, redirect
from .models import Hotelcounts

def index(request):
    hotel_data = Hotelcounts.objects.all()
    return render(request, 'inneats_app/index.html', {'hotel_data':hotel_data})
    
def about(request):    
    return render(request, 'inneats_app/about.html')

def property_list(request):
    return render(request, 'inneats_app/property-list.html')

def property_type(request):     
    return render(request, 'inneats_app/property-type.html')

# 주석처리 -kdy
# def property_agent(request):
#     hotel_data = Hotelcounts.objects.all()
#     return render(request, 'inneats_app/properties.html', {'hotel_data':hotel_data})

def property_testimonial(request):
    return render(request, 'inneats_app/testimonial.html')

def error404(request):
    return render(request, 'inneats_app/404.html')

def contact(request):
    return render(request, 'inneats_app/contact.html')


