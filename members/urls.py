from .views import *
from django.urls import path

urlpatterns = [
    path('love/', fun),
    path('jaan/', fun2),
    path('baby/', fun3),
    path('hello/', fun4),
    path('hello/<int:courseid>', fun5),
    path('', homePage),
]