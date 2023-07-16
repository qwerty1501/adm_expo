from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView

from .models import News
from .serializers import NewsSerializer


class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer