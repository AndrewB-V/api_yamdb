from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLES = [('user', 'Аутентифицированный пользователь'),
             ('moderator', 'Модератор'),
             ('admin', 'Администратор')]

    USER = 'user'
    ADMIN = 'admin'
    MODERATOR = 'moderator'

    STAFF_ROLES = [ADMIN, MODERATOR]

    email = models.EmailField(
        'Почта',
        unique=True
    )
    bio = models.TextField(
        'Биография',
        blank=True
    )
    role = models.CharField(
        'Роль',
        max_length=100,
        blank=True,
        choices=ROLES,
        default=USER
    )
    confirmation_code = models.CharField(
        'Проверочный код',
        max_length=100,
        blank=True
    )

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    @property
    def is_user(self):
        return self.role == self.USER

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    class Meta:
        ordering = ['id']
        constraints = [
            models.UniqueConstraint(
                fields=['email', 'username'],
                name='unique_auth'
            ),
        ]
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'