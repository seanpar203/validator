from .utils.fixtures import user_validator, invalid_user_validator


def test_fields_are_valid(user_validator):
    """
    Tests that fields are valid and the `is_valid` method works correctly.
    """
    assert user_validator.is_valid()

    # Tests that keys are in data.
    assert 'email' in user_validator.data
    assert 'age' in user_validator.data
    assert 'height' in user_validator.data


def test_fields_are_invalid(invalid_user_validator):
    """
    Tests that invalid fields provide the appropriate error msg.
    """
    assert not invalid_user_validator.is_valid()

    # Tests that keys are in errors.
    assert 'email' in invalid_user_validator.errors
    assert 'age' in invalid_user_validator.errors
    assert 'height' in invalid_user_validator.errors
