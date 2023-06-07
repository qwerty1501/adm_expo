from django.urls import path
from .views import LocationListAPIView, LocationRetrieveAPIView, StandListAPIView, StandRetrieveAPIView, HotelListAPIView, HotelRetrieveAPIView, \
FeedbackListAPIView, FeedbackRetrieveAPIView, ContactsListAPIView, ContactsRetrieveAPIView

urlpatterns = [
    ############   LOCATIONS
    path('location/', LocationListAPIView.as_view()),
    path('location/<int:pk>', LocationRetrieveAPIView.as_view()),
    ############   HOTEL
    path('hotel/', HotelListAPIView.as_view()),
    path('hotel/<int:pk>', HotelRetrieveAPIView.as_view()),
    ############   STAND
    path('stand/', StandListAPIView.as_view()),
    path('stand/<int:pk>', StandRetrieveAPIView.as_view()),
    ############   Feedback
    path('feedback/', FeedbackListAPIView.as_view()),
    path('feedback/<int:pk>', FeedbackRetrieveAPIView.as_view()),
    ############   Contacts
    path('contacts/', ContactsListAPIView.as_view()),
    path('contacts/<int:pk>', ContactsRetrieveAPIView.as_view()),
]