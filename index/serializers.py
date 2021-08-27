from dataclasses import fields

from rest_framework import serializers
from .models import Feature, Media


class FeatureSerializer(serializers.ModelSerializer):
    food_media = serializers.SerializerMethodField()
    restaurant_media = serializers.SerializerMethodField()

    def get_food_media(self, obj):
        return obj.food_media()

    def get_restaurant_media(self, obj):
        return obj.restaurant_media()

    class Meta:
        model = Feature
        fields = "__all__"
        depth = 2


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = "__all__"
