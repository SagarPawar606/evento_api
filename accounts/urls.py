from django.urls import path
from .views import registeruser, UsersList, Api_home, AlterUser, RegisterUser

urlpatterns = [
    path('register/', registeruser, name='registeruser'),
    path('', Api_home.as_view(), name='api_home'),
    path('user/', UsersList.as_view(), name='users_list'),
    path('user/register/', RegisterUser.as_view(), name='user_register'),
    path('user/<int:pk>/', AlterUser.as_view(), name='get_user'),
]
