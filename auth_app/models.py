from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

from django.db import models



class UserManager(BaseUserManager):
    def create_user(self, username, name, password=None):
        if not username:
            raise ValueError('User must have username!')

        user = self.model(username=username, name=name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, name, password):
        user = self.create_user(username, name, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=100,
        unique=True,
    )

    name = models.CharField(
        max_length=255,
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = (
        'name',
    )

    objects = UserManager()

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return f'User("{self.username}")'

    class Meta:
        ordering = ('username',)



class TelegramUser(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True
    )

    chat_id = models.PositiveIntegerField(
        unique=True,
    )

    def __str__(self):
        return f'TUser({self.user.username}, {self.chat_id})'
    