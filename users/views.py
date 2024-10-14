
from django.shortcuts import render

from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import Counter
from users.tokens import gettokens
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError


# <-- check if the user exit orelse Register new user and return token as response."""
@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if User.objects.filter(username=username).exists():
        raise ValidationError(f'User with {username} username already exists.')
    
    user = User.objects.create(username=username)
    user.set_password(password)
    user.save()

    return Response(
        data=gettokens(user),  
        status=status.HTTP_201_CREATED
    )

# <-- Views for request counter -->
class RequestCounter(APIView):
   
    def get(self, request):
        counter = Counter.objects.get(key='request_count')
        
        return Response(data={'requests':counter.value})


# <--View to reset request counter.-->
class ResetRequestCounter(APIView):
    def post(self, request):

        counter = Counter.objects.get(key='request_count')
        counter.value = 0
        counter.save()

        return Response(data={'message':'request count reset successfully'})
