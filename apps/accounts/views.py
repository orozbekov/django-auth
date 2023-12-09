from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from apps.accounts.serializers import LoginSerializer, RegisterSerializer
from rest_framework import status
from rest_framework.response import Response

class RegisterView(APIView):
    
    serializer_class = RegisterSerializer

    @swagger_auto_schema(
        request_body=serializer_class,
        operation_summary='Регистрация пользователя',
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'success': 'Вы успешно зарегистрировались',
        }, status=status.HTTP_201_CREATED)


class LoginView(APIView):

    serializer_class = LoginSerializer

    @swagger_auto_schema(
        request_body=serializer_class,
        operation_summary='Авторизация пользователя',
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)