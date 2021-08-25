from django.contrib import admin
from .models import *


# Register your models here.


class MediaAdmin(admin.ModelAdmin):
    list_display = ['file','restaurant','food']
    list_filter = ['restaurant','food']
    search_fields = (
        'food__title',
        'restaurant__name'
    )

class MediaInline(admin.TabularInline):
    model = Media
    autocomplete_fields = ['user','restaurant']
    exclude = ['thumbnail']
    extra = 1



class RestaurantAdmin(admin.ModelAdmin):
    inlines = [MediaInline]
    search_fields = ['name']


class FoodAdmin(admin.ModelAdmin):
    list_display = ['title', 'restaurant']
    list_filter = ['restaurant']
    inlines = [MediaInline]


class FeatureAdmin(admin.ModelAdmin):
    pass

admin.site.register(Media, MediaAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Feature,FeatureAdmin)
