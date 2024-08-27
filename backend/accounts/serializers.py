from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'phonenumber', 'date_birth', 'address', 'city', 'street', 'floor', 'apartment', 'role', 'zip_code', 'is_deleted', 'is_active', 'register_date', 'additional_information']


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(style={'input_type': 'password'})
