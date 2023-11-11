from django.urls import path
from .views import cars
urlpatterns = [
    path('api/',cars),
]
