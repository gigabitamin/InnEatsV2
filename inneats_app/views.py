
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

def property_testimonial(request):
    return render(request, 'inneats_app/testimonial.html')

def error404(request):
    return render(request, 'inneats_app/404.html')

def contact(request):
    return render(request, 'inneats_app/contact.html')


