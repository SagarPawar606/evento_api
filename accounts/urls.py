from django.urls import path
from .views import registeruser, UsersList, Api_home, AlterUser, RegisterUser, UserProfiles
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', registeruser, name='registeruser'),
    path('', Api_home.as_view(), name='api_home'),
    path('user/', UsersList.as_view(), name='users_list'),
    path('user/register/', RegisterUser.as_view(), name='user_register'),
    path('user/<int:pk>/', AlterUser.as_view(), name='get_user'),
    path('user/profiles/', UserProfiles.as_view(), name='profiles'),

    path('api-token-auth/', obtain_auth_token, name='obtain_auth_token')
]
