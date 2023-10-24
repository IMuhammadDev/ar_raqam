from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "username",
        "email",
        "role",
        "contact_number",
        "address",
        "is_active",
        "is_staff",
    )
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {"fields": ("role", "contact_number", "address")}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {"fields": ("role", "contact_number", "address")}),
    )
