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


