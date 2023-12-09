from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator


class RegisterSerializer(serializers.ModelSerializer):
    """Сериализация регистрации пользователя"""
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True,
                                     validators=[validate_password], min_length=8, max_length=30)
    confirm_password = serializers.CharField(min_length=8, max_length=30, required=True, write_only=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')
        

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.pop('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError({'password': "Пароль не совпадает."})
        return data
    
    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': "Пользователь с таким адресом электронной почты уже существует"})
        return email
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.ModelSerializer):
    """Сериализация авторизации пользователя"""

    username = serializers.CharField(max_length=100, required=True)
    password = serializers.CharField(max_length=160, min_length=8, write_only=True)

    tokens = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('username', 'password', 'tokens')

    def get_tokens(self, instance):
        user = User.objects.get(username=instance['username'])
        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    def validate(self, data):
        username = data['username']
        password = data['password']
        
        try:
            user = User.objects.get(username=username)
            if not user.check_password(password):
                raise serializers.ValidationError({'error': 'Неверный логин или пароль.' })
        except User.DoesNotExist:
            raise serializers.ValidationError({'error': 'Неверный логин или пароль.'})    
       
        return {
            'username': user.username,
            'tokens': user.tokens
        }