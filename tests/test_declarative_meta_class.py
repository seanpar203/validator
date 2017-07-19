from validator import Field
from tests.utils.fixtures import user_validator


def test_declared_fields_being_removed(user_validator):
    """
    This tests that declared fields are removed from the object.
    """
    assert getattr(user_validator, 'email', None) is None
    assert getattr(user_validator, 'age', None) is None
    assert getattr(user_validator, 'height', None) is None


def test_declared_fields_in_fields_attr(user_validator):
    """
    This tests that fields contain the key names of defined Fields.
    """
    assert len(user_validator.fields) == 3
    assert 'email' in user_validator.fields
    assert 'age' in user_validator.fields
    assert 'height' in user_validator.fields


def test_Field_as_values_in_fields_attr(user_validator):
    """
    This tests that user_validators.fields.values() are all Fields.
    """
    values = [val for val in user_validator.fields.values()]
    for val in values:
        assert isinstance(val, Field)
