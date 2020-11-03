from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username'
        )


class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(
        style={
            'input_type': 'password'
        },
        write_only=True)

    def save(self):
        user = User(
            username=self.validated_data.get('username'),
            name=self.validated_data.get('name'),
        )

        password1 = self.validated_data.get('password')
        password2 = self.validated_data.get('password2')


        if password1 != password2:
            raise serializers.ValidationError({
                'password': 'Password\'s didn\'t match.'
            })
        user.set_password(password1)

        user.save()

        return user

    class Meta:
        model = User
        fields = [
            'username',
            'name',
            'password',
            'password2'
        ]

        extra_kwargs = {
            'password': {
                'write_only': True,
            }
        }