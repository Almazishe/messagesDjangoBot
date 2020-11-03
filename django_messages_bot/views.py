from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .bot import bot
from django_tgbot.types.update import Update

import logging


@csrf_exempt
def handle_bot_request(request):
    update = Update(request.body.decode("utf-8"))
    
    try:
        bot.handle_update(update)
    except Exception as e:
        if settings.DEBUG:
            raise e
        else:
            logging.exception(e)
    return HttpResponse("OK")
