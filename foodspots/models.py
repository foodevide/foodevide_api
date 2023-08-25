from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class FoodSpot(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='foodspot_images/')  # Configure MEDIA_ROOT and MEDIA_URL in your settings.
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    time = models.CharField(max_length=100)
    location = models.CharField(max_length=255)  # Store coordinates as a string, e.g., "latitude,longitude"
    categories = models.ManyToManyField(Category)
    reel = models.URLField(blank=True, null=True)
    def __str__(self):
        return self.name
