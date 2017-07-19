from .utils.fixtures import user_validator
from .utils.validator_functions import TestValidators


def test_field_validator_functions(user_validator):
    """
    This test makes sure that the defined functions are present.

    Note:
        Unfortunately for our dynamic functions like `is_gt_than` we can't
        check because it returns a closure, but just knowing that the static
        functions are present in the fields validators list is good enough.
    """
    email_field = user_validator.fields['email']

    assert TestValidators.is_email in email_field.validators


def test_field_attribute_after_validation(user_validator):
    assert getattr(user_validator, 'email', None) is None

    user_validator.is_valid()

    assert user_validator.email == user_validator.data['email']
