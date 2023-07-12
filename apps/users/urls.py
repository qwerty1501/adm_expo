from django.urls import path
from knox import views as knox_views

from apps.users.views import UserMVS, RegisterCreateListView, RegisterDeleteView, CustomTokenRefreshView, LoginAPI

from . import views

userPlural = {
    'get': 'list',
    'post': 'create'
}

useSingle = {
    'get': 'retrieve',
    'patch': 'update'
}

useSingle2 = {
    'get': 'retrieve',
    'post': 'create',
}

useSingle3 = {
    'get': 'retrieve',
    'patch': 'update',
    'post': 'create',
    'delete': 'destroy'
}

urlpatterns = [
    path('user/', UserMVS.as_view(userPlural)),
    path('user/<uuid:uniqueId>/', UserMVS.as_view(useSingle)),
    
    path('registration/', RegisterCreateListView.as_view()),
    path('registration/<int:pk>', RegisterDeleteView.as_view()),

    path('check/', CustomTokenRefreshView.as_view()),

    # path('login/', views.UserLogin.as_view()),

    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
