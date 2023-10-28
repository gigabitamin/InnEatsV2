from django.shortcuts import render

def search(request, property_type, location, search_input):
    context = {
        'property_type': property_type,
        'location': location,
        'search_input': search_input,
    }
    return render(request, 'search.html', context)
