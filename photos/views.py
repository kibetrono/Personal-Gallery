from django.shortcuts import render
from .models import Image, Location, Category
from django.contrib import messages
from django.http import Http404


# Create your views here.

def home(request):
    image = Image.objects.all()
    location = Location.objects.all()
    category = Image.objects.all()
    title = "Home - Page"
    context = {'title': title, 'images': image[:8], 'locations': location, 'categories': category}
    return render(request, 'photos/home.html', context)

