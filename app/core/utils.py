"""
Util functionalities.
"""
from django.contrib.auth import get_user_model
from core.models import User


def create_user(email: str = 'test@example.com', password: str = 'sample123',
                name: str = 'Test', is_super: bool = False) -> User:
    """Create and return user."""
    user = get_user_model().objects.create_user(
        email=email,
        password=password,
        name=name,
    )
    if is_super:
        """Changing normal user to superuser."""
        get_user_model().objects.promote_to_superuser(user=user)

    return user
