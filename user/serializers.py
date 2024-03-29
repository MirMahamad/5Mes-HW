import re
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from user.models import ConfirmUserCode

class UserValidateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(min_length=8)

    def validate_password(self, password):
        if re.match('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$', password):
            raise ValidationError('Password should consist only letters and numbers!')
        return password


class UserLoginValidateSerializer(UserValidateSerializer):
    pass


class UserCreateValidateSerializer(UserValidateSerializer):
    is_active = serializers.BooleanField(required=False, default=False)

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('User already exists!')


class ConfirmCodeValidateSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    code = serializers.CharField(min_length=6, max_length=6)

    def validate_product_id(self, user_id):
        try:
            ConfirmUserCode.objects.get(id=user_id)
        except ConfirmUserCode.DoesNotExist:
            raise ValidationError(f'Director with id ({user_id}) not found')
        return user_id
