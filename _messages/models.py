from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()

class Message(models.Model):
    from_user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='from_me_messages'
    )

    to_user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='to_me_messages'
    )

    text = models.TextField(
        blank=False,
        null=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'Message from {self.from_user.username} to {self.to_user.username}'
    