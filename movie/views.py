from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth
import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Load environment variables 
load_dotenv('D://PROJECTDJANGO//movie_api_management//movie//api_credentials.env')
API_URL = 'https://demo.credy.in/api/v1/maya/movies/'
API_USERNAME = os.environ.get('USERNAME')
API_PASSWORD = os.environ.get('PASSWORD')


# <--- fetches a list of movies from a third-party API using Basic Authentication -->
@api_view(['GET'])
def maya_movie_api(request):
    
    page = request.query_params.get('page')

    try:
        response = requests.get(
            API_URL,
            auth=HTTPBasicAuth(API_USERNAME, API_PASSWORD),
            params={'page': page} if page else None,
            timeout=10 
        )
        response.raise_for_status()  
    except requests.exceptions.RequestException as e:
       
        return Response({"error": str(e)}, status=status.HTTP_502_BAD_GATEWAY)

    # Return the response JSON if successful
    return Response(response.json(), status=response.status_code)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Collection, Movie
from .serializers import CollectionSerializer, MovieSerializer
from django.db.models import Count


#  <--- Get all collections with top 3 favorite genres.-->
@api_view(['GET'])
def get_collections(request):
   
    collections = Collection.objects.all()
    collection_data = CollectionSerializer(collections, many=True).data

    genre_count = Movie.objects.values('genres').annotate(genre_count=Count('genres')).order_by('-genre_count')[:3]
    favourite_genres = ', '.join([genre['genres'] for genre in genre_count])

# <-- return the movie collection list
    return Response({
        'is_success': True,
        'data': {
            'collections': collection_data,
            'favourite_genres': favourite_genres
        }
    }, status=status.HTTP_200_OK)


# <-- creates a new movie collection -->
@api_view(['POST'])
def create_collection(request):
    """Create a new collection with movies."""
    data = request.data
    movies_data = data.pop('movies', [])

    collection = Collection.objects.create(**data)

    for movie in movies_data:
        Movie.objects.create(collection=collection, **movie)

    return Response({'collection_uuid': collection.uuid}, status=status.HTTP_201_CREATED)


# <-- Update collection's title, description, or movie list.-->
@api_view(['PUT'])
def update_collection(request, collection_uuid):
    
    try:
        collection = Collection.objects.get(uuid=collection_uuid)
    except Collection.DoesNotExist:
        return Response({'error': 'Collection not found'}, status=status.HTTP_404_NOT_FOUND)

    data = request.data

    collection.title = data.get('title', collection.title)
    collection.description = data.get('description', collection.description)
    collection.save()

    if 'movies' in data:
        collection.movies.all().delete()
        for movie_data in data['movies']:
            Movie.objects.create(collection=collection, **movie_data)

    return Response({'message': 'Collection updated successfully'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_collection_detail(request, collection_uuid):
    # <--Get details of a specific collection.-->
    try:
        collection = Collection.objects.get(uuid=collection_uuid)
    except Collection.DoesNotExist:
        return Response({'error': 'Collection not found'}, status=status.HTTP_404_NOT_FOUND)

    collection_data = CollectionSerializer(collection).data
    return Response(collection_data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_collection(request, collection_uuid):
    # <--Delete a collection.-->
    try:
        collection = Collection.objects.get(uuid=collection_uuid)
    except Collection.DoesNotExist:
        return Response({'error': 'Collection not found'}, status=status.HTTP_404_NOT_FOUND)

    collection.delete()
    return Response({'message': 'Collection deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
