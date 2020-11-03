from django.urls import path


from rest_framework.authtoken import views

from .views import register
from .views import users_list

urlpatterns = [
    path('token', views.obtain_auth_token, name='auth-token'),
    path('register', register, name='register'),
    path('list', users_list, name='users-list')
]
