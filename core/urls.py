from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('example/', example),
    path('bar/', bar),
    path('line/', line),
    path('radar/', radar),
    path('doughnut/', doughnut),
    path('polar/', polar),
    path('bubble/', bubble),
    path('scatter/', scatter),
    path('area/', area),
]
