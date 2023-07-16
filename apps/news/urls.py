from django.urls import path

from .views import NewsListAPIView


urlpatterns = [
    path('news/', NewsListAPIView.as_view()),
    path('news/<int:pk>', NewsListAPIView.as_view())
]