from .models import Category, PageOne, Forum, Target, Tasks, Ellipse, Sectors, Place, Speakers, Organizers, Sponsors, Partners, Socials
from rest_framework import serializers as s


class RecursiveSerializer(s.Serializer):

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CategorySerializer(s.ModelSerializer):
    children = RecursiveSerializer(many=True)

    class Meta:
        model = Category
        fields = 'id', 'name', 'icon', 'image', 'children',
        
        
class PageOneSerializer(s.ModelSerializer):
    
    class Meta:
        model = PageOne
        


class FormSerializer(s.ModelSerializer):
    pass


class TargetSerializer(s.ModelSerializer):
    pass 


class TasksSerializer(s.ModelSerializer):
    pass


class EllipseSerializer(s.ModelSerializer):
    pass


class SectorsSerializer(s.ModelSerializer):
    pass


class PlaceSerializer(s.ModelSerializer):
    pass


class SpeakersSerializer(s.ModelSerializer):
    pass


class OrganizersSerializer(s.ModelSerializer):
    pass


class SponsorsSerializer(s.ModelSerializer):
    pass


class PartnersSerializer(s.ModelSerializer):
    pass


class SociolsSerializer(s.ModelSerializer):
    pass