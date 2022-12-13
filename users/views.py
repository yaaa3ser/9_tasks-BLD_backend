from rest_framework import generics , permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import *
from knox.auth import TokenAuthentication
from rest_framework import status

class DetailedUser(generics.GenericAPIView):
    # default auth is token auth ===> see settings.py
    # REST_FRAMEWORK = {
    #     'DEFAULT_AUTHENTICATION_CLASSES': [
    #         'knox.auth.TokenAuthentication',
    #     ]
    # }
    serializer_class = UserSerializer
    
    def get(self,request,pk):
        try:
            user = User.objects.get(id=pk)
            return Response(UserSerializer(user).data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND, data="User Not Found")
        
    def put(self,request,pk):
        if request.user.id == pk:
            try :
                user = User.objects.get(id=pk)
            except :
                return Response("User Not Found!")
            serializer = UserSerializer(user,data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("Updated Successfully!")
            else :
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else :
            return Response("You Don't Have Access !")
        
    def patch(self,request,pk):
        if request.user.id == pk:
            try :
                user = User.objects.get(id=pk)
            except :
                return Response("User Not Found!")
            serializer = UserSerializer(user,data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response("Updated Successfully!")
            else :
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        else :
            return Response("You Don't Have Access !")