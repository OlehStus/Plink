from django.shortcuts import render
from rest_framework import generics
from .serializers import MyUserDetailSerializer, MyUserListSerializer
from .models import MyUser
from .pemissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class MyUserCreateView(generics.CreateAPIView):
    serializer_class = MyUserDetailSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        return Response(user_data, status=status.HTTP_201_CREATED)

class MyUserListView(generics.ListAPIView):
    serializer_class = MyUserListSerializer
    queryset = MyUser.objects.all()
    permission_classes = (IsAuthenticated, )


class MyUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MyUserDetailSerializer
    queryset = MyUser.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )