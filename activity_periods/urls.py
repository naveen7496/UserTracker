from django.urls import path
from . import views

urlpatterns = [
    path('userdetails/', views.user_details, name='user-details'),
]