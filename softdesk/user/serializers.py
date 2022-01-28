from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'id']


class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'username', "password"]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = User(email=self.validated_data['email'],
                       username=self.validated_data['username'],)
        password = self.validated_data['password']
        account.set_password(password)
        account.save()
        return account
