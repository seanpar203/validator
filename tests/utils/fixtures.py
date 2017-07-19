import pytest

from .data import user_data
from .validators import UserValidator


@pytest.fixture
def user_validator():
    """
    Used to simplify test cased and reduce verbosity.
    """
    return UserValidator(user_data)
