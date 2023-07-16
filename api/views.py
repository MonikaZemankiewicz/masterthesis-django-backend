from django.shortcuts import render
from rest_framework import generics
from .serializers import PictureSerializer
from .models import Picture


class PictureView(generics.ListAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
