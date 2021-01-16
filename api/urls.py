from django.urls import path
from .views import *


urlpatterns = [
    path('v1/api/', api_watson),
]