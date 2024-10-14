
from django.urls import path, include
from . import views   


from django.urls import path
from .views import *

urlpatterns = [
    path('',maya_movie_api, name='movieapi')
]