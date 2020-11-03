from django_tgbot.decorators import processor
from django_tgbot.state_manager import message_types, update_types, state_types
from django_tgbot.types.update import Update
from .bot import state_manager
from .models import TelegramState
from .bot import TelegramBot




@processor(state_manager, from_states='asked_for token', message_types=message_types.Text)
def get_token(bot: TelegramBot, update: Update, state: TelegramState):
    
    bot.sendMessage(update.get_chat().get_id(), update.get_message().get_text())
    
