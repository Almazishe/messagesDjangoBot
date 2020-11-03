from django.contrib import admin


from .models import User
from .models import TelegramUser



admin.site.register(User)
admin.site.register(TelegramUser)
