import PIL
from PIL import Image
from django.contrib.auth.models import User
from django.db import models
import os.path
from django.core.files.base import ContentFile
from io import BytesIO
from .validators import validate_file_size, validate_square_shape


# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    address = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.name}"


class Food(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"


class Price(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    date = models.DateField()


class Comment(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)


class Rank(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, blank=True, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, blank=True, null=True)
    rank = models.PositiveSmallIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Feature(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    def __str__(self):
        return f"{self.food.title}"


class Media(models.Model):
    file = models.FileField(validators=[validate_file_size])
    thumbnail = models.ImageField(null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, blank=True, null=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.file.name} | {self.restaurant} | {self.food}"

    def create_thumbnail(self):

        image = Image.open(self.file)
        thumbnail = image.thumbnail((250, 250), PIL.Image.ANTIALIAS)
        thumbnail_name, thumbnail_extention = os.path.splitext(self.file.path)
        thumbnail_extention = thumbnail_extention.lower()
        thumbnail_filename = thumbnail_name + '_thumb' + thumbnail_extention
        if thumbnail_extention in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        elif thumbnail_extention == '.gif':
            FTYPE = 'GIF'
        elif thumbnail_extention == '.png':
            FTYPE = 'PNG'
        else:
            return False
        temp_thumbnail = BytesIO()
        image.save(temp_thumbnail, FTYPE)
        temp_thumbnail.seek(0)

        self.thumbnail.save(thumbnail_filename, ContentFile(temp_thumbnail.read()), save=False)
        temp_thumbnail.close()
        return True

    def save(self, *args, **kwargs):
        if not self.create_thumbnail():
            raise Exception("invalid file type")
        super(Media, self).save(*args, **kwargs)
