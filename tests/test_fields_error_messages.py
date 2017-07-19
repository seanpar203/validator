from .utils.fixtures import invalid_user_validator
from .utils.validator_functions import TestValidators


def test_invalid_email_error_msg(invalid_user_validator):
    """
    Tests that the validator properly validates invalid fields.
    """
    user = invalid_user_validator
    user.is_valid()

    passed, error_msg = TestValidators.is_email(user.data['email'])
    user_errors = user.errors['email']

    assert len(user_errors) == 1
    assert error_msg in user_errors
