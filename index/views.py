from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index/index.html')


# APIs here
def test(request):
    return JsonResponse({"sina": "hi"})


def feature_api(request):

    return JsonResponse({"sina": "hi"})