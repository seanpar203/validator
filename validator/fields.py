from typing import Any
from collections import OrderedDict

FORMATTED_TYPE_NAMES = {
    'str':   'String',
    'int':   'Integer',
    'list':  'List',
    'float': 'Float',
    'dict':  'Dictionary'
}


class DeclarativeFieldsMetaclass(type):
    """
    Metaclass for removing declared Fields from Validator instances.
    """

    def __new__(mcs, name, bases, attrs):
        # Collect fields from current class.
        current_fields = []
        for key, value in list(attrs.items()):
            if isinstance(value, Field):
                current_fields.append((key, value))
                attrs.pop(key)

        attrs['fields'] = OrderedDict(current_fields)

        new_class = super().__new__(mcs, name, bases, attrs)
        return new_class


class Field:
    """ Validation Field. """

    def __init__(self, data_type: type = None, validators: list = []) -> None:
        self.data_type = data_type
        self.validators = validators

    def validate(self, val: Any) -> list:
        """ Validates value by passing into all validators

        :param val: Value to pass into validators
        :type val: Any

        :return: Errors or empty list.
        :rtype: list
        """
        errors: list = []

        if self.data_type and type(val) != self.data_type:
            formatted = FORMATTED_TYPE_NAMES[self.data_type.__name__]
            errors.append(f"'{val}' is expected to be a '{formatted}'")
            return errors

        else:
            for validator in self.validators:
                passed, err = validator(val)

                if not passed:
                    errors.append(err)

            return errors
