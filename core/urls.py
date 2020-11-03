from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('django_messages_bot/', include('django_messages_bot.urls')),

    path('api/', include([
        path('messages/', include('_messages.urls')),
        path('auth/', include('auth_app.urls')),
    ]))
]
