from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from .models import Entry
from rest_framework.parsers import JSONParser
from .serializers import EntrySerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Create your views here.

def index(request):
    return render(request, "main/index.html")

def login_view(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        print(username, password)

        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return HttpResponseRedirect(reverse("index"))

def logout_view(request):
    logout(request)
    return render(request, "main/index.html")

class LoginApiView(APIView):

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')

        print(username, password)

        authenticated_user = authenticate(request, username=username, password=password)

        if authenticated_user is not None:

            serializer = UserSerializer(authenticated_user)
            token = Token.objects.get(user=authenticated_user).key

            login(request, authenticated_user)

            return Response({'user':serializer.data ,'token': token }, status=status.HTTP_201_CREATED)

            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserRegisterApiView(APIView):

    # def get(self, request):
    #     users = User.objects.all()
    #     serializer = UserSerializer(users, many=True)
    #     return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=serializer.data['username'])
            token = Token.objects.create(user=user)
            return Response({'data': serializer.data, 'token': token.key }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EntriesApiView(APIView):
    
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        entries = Entry.objects.filter(owner=request.user)
        serializer = EntrySerializer(entries, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EntrySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EntryApiView(APIView):

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        
        try:
            return Entry.objects.get(pk=id)
        except Entry.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, id):
        entryObj = self.get_object(id)
        serializer = EntrySerializer(entryObj)
        return Response(serializer.data)

    def put(self, request, id):
        entryObj = self.get_object(id)
        serializer = EntrySerializer(entryObj ,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        entryObj = self.get_object(id)
        entryObj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
