from django.contrib import admin
from .models import *


# Register your models here.


class MediaAdmin(admin.ModelAdmin):
    pass


class RestaurantAdmin(admin.ModelAdmin):
    pass


class FoodAdmin(admin.ModelAdmin):
    pass


admin.site.register(Media, MediaAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Food, FoodAdmin)
