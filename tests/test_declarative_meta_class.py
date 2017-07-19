from typing import Dict, Any
from validator import Validator
from validator.fields import Field

import pytest

from tests.utils import TestValidators, user_test_data, UserValidator


@pytest.fixture
def validator():
    """
    Used to simplify test cased and reduce verbosity.
    """
    return UserValidator(user_test_data)


def test_declared_fields_being_removed(validator):
    """
    This tests that declared fields are removed from the object.
    """
    assert getattr(validator, 'email', None) is None
    assert getattr(validator, 'age', None) is None
    assert getattr(validator, 'height', None) is None


def test_declared_fields_in_fields_attr(validator):
    """
    This tests that fields contain the key names of defined Fields.
    """
    assert len(validator.fields) == 3
    assert 'email' in validator.fields
    assert 'age' in validator.fields
    assert 'height' in validator.fields


def test_Field_as_values_in_fields_attr(validator):
    """
    This tests that Validators.fields.values() are all Fields.
    """
    values = [val for val in validator.fields.values()]
    for val in values:
        assert isinstance(val, Field)
