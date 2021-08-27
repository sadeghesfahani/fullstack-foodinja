from django.http import HttpResponse, JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from foodinja.settings import BASE_DIR
from .models import *

# Create your views here.
from .serializers import FeatureSerializer, MediaSerializer


def index(request):
    return render(request, 'index/index.html')


# APIs here
def test(request):
    return JsonResponse({"sina": "hi"})


def feature_api(request):
    feature_list = Feature.objects.all()
    data = dict()
    data['feature'] = list()
    temp_data = dict()
    for feature in feature_list:

        temp_data['title'] = feature.food.title
        temp_data['body'] = feature.food.description
        temp_data['id'] = feature.food.id
        try:
            real_path = Media.objects.filter(food=feature.food).get().file.path
            base_path = str(BASE_DIR)
            print(real_path)
            print(base_path)
            excluded_path = real_path[real_path.find(base_path) + len(base_path) + 1:]
            while '\\' in excluded_path:
                excluded_path = excluded_path.replace('\\', "/", 1)
            print(excluded_path)
            temp_data['img'] = excluded_path
        except:
            temp_data['img'] = '/noimage.jpeg'
        temp_data['url'] = "/food"
        data['feature'].append(temp_data)
        temp_data = dict()
    print(request.build_absolute_uri("/"))
    data['base_location'] = str(BASE_DIR)
    data['base_url'] = request.build_absolute_uri("/")
    return JsonResponse(data)


def food_api(request, id):
    food = None
    data = dict()
    if Food.objects.filter(pk=id).exists():
        food = Food.objects.filter(pk=id).get()
        data['title'] = food.title
        data['description'] = food.description
        restaurant = Restaurant.objects.get(id=food.restaurant.id)
        data['restaurant_name'] = restaurant.name
        data['restaurant_description'] = restaurant.description
        data['restaurant_address'] = restaurant.address
        if Media.objects.get(food=food.id).exists():
            data['food_pictures'] = [pic for pic in Media.objects.filter(food=food.id)]
        if Media.objects.get(restaurant=restaurant.id).exists():
            data['restaurant_pictures'] = [pic for pic in Media.objects.filter(restaurant=restaurant.id)]
        data['food_prices'] = [price for price in Price.objects.filter(food=food.id).order_by('food__price__date')]
        data['comments'] = [comment for comment in Comment.objects.filter(food=food.id).order_by('date')]
    return JsonResponse({"data": food})


def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})


@api_view(['GET'])
def FeatureList(request):
    features = Feature.objects.all()
    # media = Media.objects.all()
    # feature_serializer = FeatureSerializer(features, many=True)
    # media_serialize = MediaSerializer(media, many=True)
    # serializer = {'feature': feature_serializer.data, "media": media_serialize.data}
    serializer = FeatureSerializer(features,many=True)
    return Response(serializer.data)
