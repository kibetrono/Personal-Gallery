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

