from django.conf import settings

from rest_framework import viewsets, permissions, status, generics
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenRefreshView

from apps.users.models import User
from apps.users.serializers import (
    UserCRUDSerializer, UserSerializer,
    CustomTokenRefreshSerializer, LoginSerializer
)


class MVSDynamicPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'update':
            if request.user.is_authenticated:
                return True
            else:
                return False
        else:
            return True


class UserMVS(viewsets.ModelViewSet):
    queryset = User.objects.all();
    permission_classes = [MVSDynamicPermission]
    lookup_field = 'uniqueId'
    serializer_class = UserSerializer

    def create(self, request):
        secretAdminKey = request.data.get('secretAdminKey');
        if secretAdminKey == settings.SECRET_ADMIN_KEY:
            serializer = UserCRUDSerializer(data={'password': settings.DEFAULT_PASSWORD}, context={'request': request});
            serializer.is_valid(raise_exception=True);
            serializer.save();
            return Response(data=f"{settings.CLIENT_URL}/user/{serializer.data['uniqueId']}");
        return Response(status=status.HTTP_403_FORBIDDEN);

    def update(self, request, *args, **kwargs):
        user = request.user;
        data = request.data.dict();
        serializer = UserCRUDSerializer(user, data=data, context={'request': request});
        serializer.is_valid(raise_exception=True);
        serializer.save();
        return Response(serializer.data);
    
    
class RegisterCreateListView(generics.ListCreateAPIView):
    queryset = User.objects.all();
    serializer_class = UserSerializer
    
    
class RegisterDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all();
    serializer_class = UserSerializer
    


class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer