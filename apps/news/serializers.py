from rest_framework import serializers as s

from .models import News


class NewsSerializer(s.Serializer):

    class Meta:
        model = News
        fields = 'image', 'title', 'description', 'urls', 'data', 'id'