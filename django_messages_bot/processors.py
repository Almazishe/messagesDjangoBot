from django_tgbot.decorators import processor
from django_tgbot.state_manager import message_types, update_types, state_types
from django_tgbot.types.update import Update
from django_tgbot.exceptions import ProcessFailure
from .bot import state_manager
from .models import TelegramState
from .bot import TelegramBot

from rest_framework.authtoken.models import Token

@processor(state_manager, from_states=state_types.All)
def get_token(bot: TelegramBot, update: Update, state: TelegramState):
    chat_id = update.get_chat().get_id()
    token_body = update.get_message().get_text()

    bot.sendMessage(chat_id, update.get_message())
    bot.sendMessage(chat_id, update.get_chat())

    # tokens = Token.objects.filter(
    #     key=token_body
    # )

    # if tokens.count() == 0:
    #     bot.sendMessage(chat_id, 'No user with such token.')
    #     raise ProcessFailure

    # token = tokens.first()
    