import pytest

from .data import user_data, invalid_user_data
from .validators import UserValidator


@pytest.fixture
def user_validator():
    """
    Valid user validator.
    """
    return UserValidator(user_data)


@pytest.fixture
def invalid_user_validator():
    """
    Invalid user validator.
    """
    return UserValidator(invalid_user_data)
