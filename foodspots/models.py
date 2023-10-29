from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
import os
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


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
    image = models.ImageField(upload_to=upload_to,default='default/restarant.jpg') 
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    time = models.CharField(max_length=100)
    location = models.CharField(max_length=255, unique=True) 
    categories = models.ManyToManyField(Category)
    reel = models.URLField(blank=True, null=True, unique=True)
    def __str__(self):
        return self.name

def compress_image(image, width=1200):
    img = Image.open(image)
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    height = int((width / float(img.width)) * float(img.height))
    img = img.resize((width, height), Image.Resampling.LANCZOS)
    output = BytesIO()
    img.save(output, format='JPEG', quality=95)
    output.seek(0)
    compressed_image = InMemoryUploadedFile(output, 'ImageField', f'{image.name.split(".")[0]}.jpg', 'image/jpeg',
                                            output.getbuffer().nbytes, None)
    return compressed_image


@receiver(pre_save, sender=FoodSpot)
def compress_foodspot_image(sender, instance, **kwargs):
    if instance.image:
        instance.image = compress_image(instance.image)

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