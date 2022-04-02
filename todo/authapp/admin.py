from django.contrib import admin
from .models.users import UserDRF
from django.contrib.auth.admin import UserAdmin


@admin.register(UserDRF)
class DirectionsAdmin(UserAdmin):
    list_display = ('email',)
    search_fields = ('email',)
