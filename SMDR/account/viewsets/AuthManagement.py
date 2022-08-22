from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, ListAPIView
from rest_framework import parsers, renderers, status
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta, datetime
import jwt
from rest_framework_jwt.settings import api_settings
from rest_framework import viewsets, permissions, generics, status, mixins
from account.models import User, Relatives
from rest_framework.schemas import SchemaGenerator
from django.db.models import Q
from rest_framework.decorators import action
from django.db import IntegrityError

from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model

import logging

from django.core.exceptions import ObjectDoesNotExist
import os
from django.db.models import Q
from django.contrib.auth import authenticate
from rest_framework.filters import SearchFilter
from account.serializers import UserSerializer, ReadUserSerializer, LoginSerializer, RelativesSerializer


class RegisterUserView(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            if get_user_model().objects.filter(email=request.data.get('email')).exists():
                return Response(
                    {'message': "User with email exists"}, status=400)
            user = serializer.create(serializer.validated_data)
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            if api_settings.JWT_ALLOW_REFRESH:
                payload['orig_iat'] = timegm(datetime.utcnow().utctimetuple()
                                             )
            data = ReadUserSerializer(user).data
            return Response({'token': jwt_encode_handler(
                payload), 'user': data}, status=200)

        else:
            return Response(serializer.errors, status=200)


class RegisterDoctorView(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            if get_user_model().objects.filter(email=request.data.get('email')).exists():
                return Response(
                    {'message': "User with email exists"}, status=400)
            user = serializer.create(serializer.validated_data)
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            if api_settings.JWT_ALLOW_REFRESH:
                payload['orig_iat'] = timegm(datetime.utcnow().utctimetuple()
                                             )
            data = ReadUserSerializer(user).data
            return Response({'token': jwt_encode_handler(
                payload), 'user': data}, status=200)

        else:
            return Response(serializer.errors, status=200)


class LoginAPIView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            email = serializer.data['email']
            password = serializer.data['password']
            user = authenticate(email=email, password=password)
            if user:
                jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
                payload = jwt_payload_handler(user)
                if api_settings.JWT_ALLOW_REFRESH:
                    payload['orig_iat'] = timegm(datetime.utcnow().utctimetuple()
                                                 )
                data = ReadUserSerializer(user).data
                return Response({'token': jwt_encode_handler(
                    payload), 'user': data}, status=200)
            return Response({'error': "Invalid Credentials"}, status=400)
        return Response(serializer.errors, status=400)


class GetProfile(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = get_user_model().objects.get(id=request.user.id)
        user = ReadUserSerializer(user)
        return Response(user.data, status=200)


class VerifyDoctor(APIView):
    permission_classses = (permissions.IsAuthenticated)

    def get(self, request):
        user = get_user_model().objects.get(id=request.user.id)
        user.is_doctor = True
        user.save()
        user = ReadUserSerializer(user)
        return Response(user.data, status=200)


class RelativesViewSets(viewsets.ModelViewSet):
    serializer_class = RelativesSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Relatives.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer = serializer.save(patient=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)

    def update(self, request, pk=None):
        serializer = self.serializer_class(instance=self.get_object())
        if serializer.is_valid():
            serializer = serializer.save(patient=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)

    def get_queryset(self):
        return self.queryset.filter(Q(relative=self.request.user) | Q(patient=self.request.user))
