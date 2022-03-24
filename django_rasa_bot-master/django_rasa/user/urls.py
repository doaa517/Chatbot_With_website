from django.urls import path

from .views import LoginApi, UserLogin, UserLogout, profile
from rest_framework.authtoken.views import obtain_auth_token

app_name="user"

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('login-api/', LoginApi.as_view(), name='login-api'),
]