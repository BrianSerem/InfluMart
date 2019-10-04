from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

from InfluMart.apps.authentication.models import User


class RegistrationSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()

    password = serializers.CharField(
        max_length=128,
        min_length=6,
        write_only=True,
        error_messages={
            "min_length": "Password should be at least {min_length} characters"
        }
    )
    confirm_password = serializers.CharField(
        max_length=128,
        min_length=6,
        write_only=True,
        error_messages={
            "min_length": "Password should be at least {min_length} characters"
        }
    )

    def validate(self, data):

        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({
                "passwords": "ensure you provide matching passwords"
            })

        try:
            validate_password(data['password'])

        except ValidationError as identifier:
            raise serializers.ValidationError({
                "password": str(identifier).replace(
                    "["", "").replace(""]", "")})
        return data

    def create(self, validated_data):

        del validated_data['confirm_password']
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name",
                  "password", "confirm_password", "username"]