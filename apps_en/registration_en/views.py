from django.shortcuts import render
from rest_framework import generics

from .serializers import ApplicationENSerializer
from .models import ApplicationEN


class ApplicationENCreateListView(generics.ListCreateAPIView):
    serializer_class = ApplicationENSerializer
    queryset = ApplicationEN.objects.all()
    
    
class ApplicationENDeleteView(generics.DestroyAPIView):
    serializer_class = ApplicationENSerializer
    queryset = ApplicationEN.objects.all()