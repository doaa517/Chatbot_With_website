from django.urls import path

from .views import UserLogin, UserLogout, profile

app_name="user"

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
]