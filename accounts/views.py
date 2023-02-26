from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User

from accounts.models import UserProfile
from .forms import UserRegistrationForm
from .serializers import GetUserSerializer, RegisterUserSerializer, ProfileSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
# Create your views here.

def registeruser(request):
    ''' User registration form view '''
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'User {username} has been registered successfully!')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts\index.html', {'form':form})

class Api_home(APIView):
    def get(self, request):
        api_routes = {'user registration form' : '/register',
                    'all users' : '/user',
                    'get/alter/delete user' : '/user/<id>',
                    'register user' : '/user/register'
                    }
        print(self.request.user)
        return Response(api_routes, status=HTTP_200_OK)


class UsersList(APIView):
    ''' returns all the registered users '''
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = GetUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GetUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=HTTP_400_BAD_REQUEST)

class RegisterUser(APIView):
    ''' user registration api endpoint view '''
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            saved_user = serializer.save()
            data['username'] = saved_user.username
            data['email'] = saved_user.email
            status = HTTP_201_CREATED
        else:
            data['errors'] = serializer.errors
            status = HTTP_400_BAD_REQUEST
        return Response(data, status)

class AlterUser(APIView):
    ''' get/alter/delete a perticular user (only by admin user)'''
    permission_classes = [IsAdminUser]
    
    @staticmethod
    def get_user(pk):
        return get_object_or_404(User, id=pk)
        
    def get(self, request, pk):
        user = self.get_user(pk)
        # if not user:
        #     return Response(status=HTTP_404_NOT_FOUND)
        serializer = GetUserSerializer(user)
        print(self.request.user)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def put(self, request, pk):
        user = self.get_user(pk)
        serializer = GetUserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response(serializer.errors ,status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        user = self.get_user(pk)
        user.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class UserProfiles(APIView):
    def get(self, request):
        profiles = UserProfile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
        