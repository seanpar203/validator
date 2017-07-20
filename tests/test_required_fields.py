from .utils.fixtures import missing_user_validator as user


def test_required_fields_error(user):
    """
    Tests that required fields don't pass validation.
    """
    user.is_valid()

    assert len(user.errors['email']) == 1
    assert user.errors['email'][0] == 'email field is required.'
