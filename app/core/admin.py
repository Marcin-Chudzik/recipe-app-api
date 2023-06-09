"""
Django admin customization.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import (
    User,
    Recipe,
    Tag,
    Ingredient,
)

"""Registering the simple models."""
MODELS = [Recipe, Tag, Ingredient]

[admin.site.register(model_name) for model_name in MODELS]


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['username', 'email', 'name']
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser'
            )
        }),
    )


# @admin.register(Recipe)
# class RecipeAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     pass
