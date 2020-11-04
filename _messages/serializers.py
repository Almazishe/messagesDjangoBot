from .models import Message
from rest_framework import serializers


from django.contrib.auth import get_user_model
User = get_user_model()


from django_messages_bot.bot import bot
from auth_app.models import TelegramUser


def sendMessage(from_user, to_user, text):
    tg_users = TelegramUser.objects.filter(user__id=to_user.id)
    if tg_users.count() == 0:
        return
    bot.sendMessage(tg_users.first().chat_id, f'{from_user.usename}, я получил от тебя сообщение:\n{text}')

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

        sendMessage(request.user, to_user.first(), self.validated_data.get('text'))

        return message

    class Meta:
        model = Message
        fields = (
            'to_user_id',
            'text'
        )
