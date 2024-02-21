from django.contrib import admin
from rest_framework_simplejwt import token_blacklist

from .models import User, Profile


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'auth_provider', 'created_at', 'id']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'created_at']


admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)

