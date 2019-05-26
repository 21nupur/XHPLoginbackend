from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = CustomUser.objects.create(
            username=validated_data['username'],
            date_of_birth=validated_data['date_of_birth'],
            phone=validated_data['phone'],
            email=validated_data['email'],
            address=validated_data['address'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = CustomUser
        fields = ("id", 'username', 'password', 'first_name', 'last_name', "date_of_birth", "phone", "email", 'address')


class UserDetailSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = '__all__'