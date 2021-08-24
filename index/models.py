from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Restaurant(models.Model):
    description = models.CharField(max_length=1000)
    address = models.CharField(max_length=500)
    link = models.JSONField()


class Food(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    link = models.JSONField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


class Price(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    date = models.DateField()


class Comment(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)


class Rank(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    rank = models.PositiveSmallIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Feature(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()

