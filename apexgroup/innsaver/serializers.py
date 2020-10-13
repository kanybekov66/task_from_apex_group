from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Human

class HumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = ['surname', 'firstName', 'patronymic', 'adress', 'phoneNumber']


class CreateHumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = ['surname', 'firstName', 'patronymic', 'adress', 'phoneNumber', 'inn']
        extra_kwargs = {
            'surname' : {'write_only':True},
            'firstName' : {'write_only':True},
            'patronymic' : {'write_only':True},
            'adress' : {'write_only':True},
            'phoneNumber' : {'write_only':True},
            'inn' : {'write_only':True}
            }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password' : {'write_only':True, 'required':True}}
    

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user