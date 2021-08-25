from django.urls import path
from index import views

urlpatterns = [
    path('', views.index),
    path('test', views.test),
    path('feature', views.feature_api, name='feature')
]
