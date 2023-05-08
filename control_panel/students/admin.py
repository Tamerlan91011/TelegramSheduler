from django.contrib import admin
from .models import User,Group

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "student_card_number", "password", "telegram_chat_number", "group"]


class UserGroup(admin.ModelAdmin):
    list_display = ["name"]

admin.site.register(User, UserAdmin)
admin.site.register(Group, UserGroup)