from .models import Message
from rest_framework import serializers

from django.contrib.auth import get_user_model
User = get_user_model()


class SendMessageSerializer(serializers.ModelSerializer):
    to_user_id = serializers.IntegerField()

    def save(self):
        request = self.context['request']
        to_user = User.objects.filter(
            id=self.validated_data.get('to_user_id'),
        )

        if to_user.count() == 0:
            raise serializers.ValidationError({
                'to_user_id': 'No user with such ID.'
            })


        message = Message(
            from_user=request.user,
            to_user=to_user.first(),
            text=self.validated_data.get('text')
        )
        message.save()
        return message

    class Meta:
        model = Message
        fields = (
            'to_user_id',
            'text'
        )
