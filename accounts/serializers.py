from rest_framework import serializers
from django.contrib.auth import get_user_model

from accounts.send_email import send_code_email

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(min_length=6, write_only=True, )
    password2 = serializers.CharField(min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ("email", "password1", "password2", "full_name")
        extra_kwargs = {
            "full_name": {"required": True}
            }


    def validate_email(self, data):
        result = User.objects.filter(email=data).exists
        if not result:
            raise serializers.ValidationError("already exists!!!")
        return data

    def validate(self, attrs):
        password = attrs.pop('password1')
        password2 = attrs.pop('password2')
        if password != password2:
            raise serializers.ValidationError("don't match")
        attrs['password'] = password
        return attrs

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.create_activation_code()
        user.save()
        send_code_email(user)
        return user