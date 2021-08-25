from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from foodinja.settings import BASE_DIR
from .models import *


# Create your views here.
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
        print("jere")
        try:
            real_path = Media.objects.filter(food=feature.food).get().thumbnail.path
            base_path = str(BASE_DIR)
            print(real_path)
            print(base_path)
            excluded_path = real_path[real_path.find(base_path) + len(base_path) + 1:]
            while r'/' in excluded_path:
                excluded_path = excluded_path.replace('/', "\\",1)
            print(excluded_path)
            temp_data['img'] = excluded_path
        except:
            temp_data['img'] = '/noimage.jpeg'
        temp_data['url'] = "/"
        data['feature'].append(temp_data)
        temp_data = dict()

    data['base_location'] = str(BASE_DIR)
    data['base_url'] = request.build_absolute_uri("/")
    return JsonResponse(data)
