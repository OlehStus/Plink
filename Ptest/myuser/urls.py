from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'myusers'

urlpatterns = [
    path('myusers/create/', MyUserCreateView.as_view()),
    path('all/', MyUserListView.as_view()),
    path('myusers/detail/<int:pk>/', MyUserDetailView.as_view()),

]