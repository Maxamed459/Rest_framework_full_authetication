from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegisterSerializer, UserLoginSerializer
from .utils import send_email_user
from .models import User, OneTimePassword
from rest_framework.permissions import IsAuthenticated


class RegisterUserView(GenericAPIView):

    serializer_class = UserRegisterSerializer

    def post(self, request):
        user_data = request.data
        serializer = self.get_serializer(data = user_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user = serializer.data
            # print(user)
            # send email to the registered user
            send_email_user(user['email'])
            return Response({
                "user": user,
                "message": f"hi Thunk you for registering, welcome to the platform."
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyUserEmail(GenericAPIView):
    def post(self, request):
        otpcode = request.data.get("otp")
        try:
            user_code_obj = OneTimePassword.objects.get(code=otpcode)
            user = user_code_obj.user
            if not user.is_verified:
                user.is_verified = True
                user.save()
                return Response({
                    "message": "Account email verified successfully."
                }, status=status.HTTP_200_OK)
            return Response({ 
                "message": "otp code is invalid account already is verified."
            }, status=status.HTTP_400_BAD_REQUEST)
        except OneTimePassword.DoesNotExist:
            return Response({
                "message": "otp code not provided"
            }, status=status.HTTP_400_BAD_REQUEST)

class LoginUserView(GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data, context={"request": request })
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class TestAuthenticationView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({
            "message": "working great"
        }, status=status.HTTP_200_OK)
