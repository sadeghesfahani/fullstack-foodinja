from django.urls import path
from index import views

urlpatterns = [
    path('', views.index),
    path('test', views.test),
    path('feature', views.feature_api, name='feature'),
    path('food/<int:id>', views.food_api, name='food'),
    path('csrf',views.csrf,name='token'),
    path('feature-list/',views.FeatureList,name = "feature-list"),
]
