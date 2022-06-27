from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'role',
        'confirmation_code',
    )
    search_fields = ('username', 'email',)
    list_filter = ('username',)
    empty_value_display = '-пусто-'