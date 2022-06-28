from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **fields):
        if email is None:
            raise TypeError('У пользователя должен быть email')

        if username is None:
            raise TypeError('У пользователя должен быть username')

        if username == 'me':
            raise ValueError(
                'Использовать имя (me) в качестве username запрещено.'
            )

        user = self.model(
            username=username, email=self.normalize_email(email), **fields
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password, **fields):
        if password is None:
            raise TypeError('У суперпользователя должен быть пароль')

        user = self.create_user(username, email, password, **fields)
        user.is_superuser = True
        user.is_staff = True
        user.role = 'admin'
        user.save()

        return user


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
