from django.shortcuts import render,redirect
from .models import Image, Location, Category
from django.contrib import messages
from django.http import Http404
from .forms import PhotoForm



# Create your views here.

def home(request):
    image = Image.objects.all()
    location = Location.objects.all()
    category = Image.objects.all()
    title = "Home - Page"
    context = {'title': title, 'images': image[:12], 'locations': location, 'categories': category}
    return render(request, 'photos/home.html', context)

def registerPhoto(request):
    location = Location.objects.all()

    form = PhotoForm()
    if request.method == "POST":
        form_results = PhotoForm(request.POST,request.FILES)
        print(form_results)
        if form_results.is_valid():

            form_results.save()
            return redirect('home')

    context = {"form": form,'locations': location}
    return render(request, 'photos/photo.html', context)



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


def location(request, image_location):
    all_locations = Location.objects.all()
    specific_location = Location.get_location_id(image_location)
    images = Image.filter_by_location(image_location)
    title = f'{specific_location} Photos'
    context = {'title': title, 'images': images, 'locations': all_locations, 'location': specific_location}
    return render(request, 'photos/location.html', context)


def category(request, category_id):
    title = "Gallery Category"
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        raise Http404()
    context = {'category': category, 'title': title}
    return render(request, "photos/category.html", context)

