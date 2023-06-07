from django.shortcuts import render
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Location, Stand, Hotel, Feedback, Contacts
from .serializers import LocationSerializer, StandSerializer, HotelSerializar, FeedbackSerializer, ContactsSerializer

##### Location
class LocationListAPIView(ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationRetrieveAPIView(RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

#####   HOTEL
class HotelListAPIView(ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializar


class HotelRetrieveAPIView(RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializar

#### STAND
class StandListAPIView(ListAPIView):
    queryset = Stand.objects.all()
    serializer_class = StandSerializer


class StandRetrieveAPIView(RetrieveAPIView):
    queryset = Stand.objects.all()
    serializer_class = StandSerializer

####  FEEDBACK
class FeedbackListAPIView(ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class FeedbackRetrieveAPIView(RetrieveAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

####  CONTACT
class ContactsListAPIView(ListAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class ContactsRetrieveAPIView(RetrieveAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer