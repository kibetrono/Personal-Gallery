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


def search(request):
    location = Location.objects.all()  # For purpose of navbar

    title = "Search"
    if 'search_query' in request.GET and request.GET["search_query"]:
        search_term = request.GET.get("search_query").lower()
        searched_results = Image.filter_by_category(search_term)

        message = f"{search_term}"
        context = {'message': message, 'results': searched_results, 'title': title, 'locations': location}

        return render(request, 'photos/search.html', context)

    else:
        messages.error(request, "You haven't searched for any term")
        message = "You haven't searched for any term"
        return render(request, 'photos/search.html', {"message": message})

