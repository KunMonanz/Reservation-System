from rest_framework.serializers import (
    ModelSerializer,
    ValidationError,
    CharField,
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Profile, User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'profile_picture']
        read_only_fields = ['id', 'user']


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    password = CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'phone_number',
            'profile',
            'password'
        ]
        read_only_fields = ['id']
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        Profile.objects.create(user=user)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if profile_data:
            profile = instance.profile
            for attr, value in profile_data.items():
                setattr(profile, attr, value)
            profile.save()


class UserLoginSerializer(ModelSerializer):
    password = CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {
            'username': {'required': True},
            'password': {'required': True},
        }
