from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from .serializers import RegisterSerializer


class LoginView(APIView):  
    authentication_classes = []
    def post(self, request, *args, **kwargs):
        # validate username and password are correct
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # once it is correct, get the user from the validated data
        user = serializer.validated_data['user']
        # make a token
        _,token = AuthToken.objects.create(user)
        
        return Response({
            'token': token,
            'user':{
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "bio": user.bio,
            }
        })
        
class RegisterView(APIView):
    def post(self, request,*args, **kwargs):
        serializer = RegisterSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        _,token = AuthToken.objects.create(user)
        return Response({
            'token': token,
            'user':{
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "bio": user.bio
            }
        })