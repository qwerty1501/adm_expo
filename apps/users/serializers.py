from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.state import token_backend
from apps.users.models import User

from djoser.serializers import UserSerializer


class UserCRUDSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=400, required=False)

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User.objects.create(**validated_data);
        if validated_data['password']:
            user.set_password(validated_data['password']);
        user.save()
        return user

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            if field == 'password':
                instance.set_password(value);
            else:
                setattr(instance, field, value)
        instance.save();
        return instance;
    

class UserAPISerializer(serializers.ModelSerializer):

    is_authenticated = serializers.CharField(max_length=400, required=False)

    class Meta:
        model = User
        exclude = ['groups', 'user_permissions', 'resetPasswordUUID', 'resetPasswordDate']


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super(CustomTokenRefreshSerializer, self).validate(attrs);
        decoded_payload = token_backend.decode(data['access'], verify=True);
        user_id = decoded_payload['user_id'];
        user = User.objects.get(id=user_id);
        data.update({
            'profile':
            UserSerializer(user, context={'request': self.context['request']}).data
        });
        return data


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',)