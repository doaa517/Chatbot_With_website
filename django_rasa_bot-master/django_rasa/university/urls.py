from django.urls import path
from . import views

app_name="university"

urlpatterns = [
    path('branches/', views.branches, name='branches'),
    path('faculties/', views.faculties, name='faculties'),
    path('courses/', views.courses, name='courses'),
    
    path('degree-api/', views.DegreeApi.as_view(), name='degree-api'),
    path('class-info-api/', views.ClassInfoApi.as_view(), name='degree-api'),
]