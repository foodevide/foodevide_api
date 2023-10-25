from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
import os

def upload_to(instance, filename):
    file_extension = filename.split('.')[-1]
    new_filename = f'foodspot_{instance.id}_{instance.name}.{file_extension}'
    return os.path.join('foodspot_images', new_filename)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class FoodSpot(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=upload_to,default='default/restarant.jpg')  # Configure MEDIA_ROOT and MEDIA_URL in your settings.
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    time = models.CharField(max_length=100)
    location = models.CharField(max_length=255, unique=True)  # Store coordinates as a string, e.g., "latitude,longitude"
    categories = models.ManyToManyField(Category)
    reel = models.URLField(blank=True, null=True, unique=True)
    def __str__(self):
        return self.name

@receiver(pre_save, sender=FoodSpot)
def delete_old_image(sender, instance, **kwargs):
    if instance.pk:  # Check if this is an existing instance being updated.
        try:
            old_instance = sender.objects.get(pk=instance.pk)
        except sender.DoesNotExist:
            return
        if not old_instance.image == instance.image:
            if old_instance.image and os.path.isfile(old_instance.image.path):
                os.remove(old_instance.image.path)