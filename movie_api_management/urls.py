"""
URL configuration for movie_api_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from users.views import register_user, RequestCounter, ResetRequestCounter
from movie import views

# main URL router for project
urlpatterns = [
    path('admin/', admin.site.urls),
    path('request-count/', include('users.urls')),
    path('movies/', views.maya_movie_api, name='all_movies'),
    path('register/', register_user, name='register-user'),
    path('collection/', views.get_collections, name='get_collections'),
    path('collection/', views.create_collection, name='create_collection'),
    path('collection/<uuid:collection_uuid>/', views.update_collection, name='update_collection'),
    path('collection/<uuid:collection_uuid>/', views.get_collection_detail, name='get_collection_detail'),
    path('collection/<uuid:collection_uuid>/', views.delete_collection, name='delete_collection'),

]
