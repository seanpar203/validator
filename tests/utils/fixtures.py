import pytest

from . import data
from .validators import UserValidator


@pytest.fixture
def user_validator():
    """
    Valid user validator.
    """
    return UserValidator(data.user_data)


@pytest.fixture
def invalid_user_validator():
    """
    Invalid user validator.
    """
    return UserValidator(data.invalid_user_data)


@pytest.fixture
def missing_user_validator():
    """
    Missing data user validator.
    """
    return UserValidator(data.missing_email_data)
