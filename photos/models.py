from django.db import models


# Create your models here.

class Location(models.Model):
    location_name = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-location_name']

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self, name):
        self.name = name
        self.save()

    @classmethod
    def get_location_id(cls, id):
        locate = Location.objects.get(pk=id)
        return locate

    def __str__(self):
        return self.location_name


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-category_name']

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self, name):
        self.name = name
        self.save()

    def __str__(self):
        return self.category_name

    @classmethod
    def search_by_category(cls, search_term):
        photo = cls.objects.filter(category_name__icontains=search_term)
        return photo


class Image(models.Model):
    image_name = models.CharField(max_length=50)
    image_description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='choose/')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self, image_name, image_description, image, location, category):
        self.image_name = image_name
        self.image_description = image_description
        self.image = image
        self.location = location
        self.category = category
        self.save()

    @classmethod
    def get_image_by_id(cls, id):
        image_res = cls.objects.get(id=id)
        return image_res

    @classmethod
    def search_image(cls, search_term):
        image_search = cls.objects.filter(image_name__icontains=search_term)
        return image_search

    @classmethod
    def filter_by_location(cls, image_location):
        images_location = cls.objects.filter(location__id=image_location)
        return images_location

    @classmethod
    def filter_by_category(cls, category):
        filtered_category = cls.objects.filter(category__category_name=category)
        return filtered_category

    def __str__(self):
        return self.image_name

# save_image() - Save an image to the database.
# delete_image() - Delete image from the database.
# update_image() - Update image in the database.
# get_image_by_id(id) - Allows us to get an image using its ID.
# search_image(category) - Allows us to search for an image using its category.
# filter_by_location(location) - Allows us to filter images by the location.
