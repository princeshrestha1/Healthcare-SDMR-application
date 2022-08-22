from .models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        min_length=8, write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'is_superuser',
            'is_admin',
            'password',
            'is_active')
        lookup_field = 'email'
        read_only_fields = ('id', 'is_superuser', 'is_admin', 'is_active')

    def get_queryset(self):
        if self.request.user.is_staff:
            return User.objects.all()
        else:
            return self.request.user

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_doctor=True,

        )
        user.set_password(validated_data['password'])
        user.save()

        reciever = [validated_data['email']]

        # send_mail(subject, message, None, recipent)
        return user

    def create_admin(self, validated_data):
        user = User(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_admin=True,
            is_staff=True
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ReadUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'avatar_url')
        lookup_field = 'email'
        # read_only_fields = "__all__"


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
