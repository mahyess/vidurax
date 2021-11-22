from django.db import transaction
from rest_framework import generics
from rest_framework.response import Response
from knox.models import AuthToken

from users.serializers import RegisterSerializer, PasswordSerializer, UserSerializer, LoginSerializer


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        with transaction.atomic():
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()

            # setting created user's password
            password_serializer = PasswordSerializer(data=request.data)
            if password_serializer.is_valid():
                user.set_password(password_serializer.data["password"])
                user.save()

            return Response(
                {
                    "user": UserSerializer(
                        user, context=self.get_serializer_context()
                    ).data,
                    "token": AuthToken.objects.create(user)[1],
                }
            )


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )
