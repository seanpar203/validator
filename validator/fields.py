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
        """
        Remove declared Fields as object attributes

        Notes:
            This is necessary to allow a declarative interface for inherited
            Validation objects. We then reset the attrs to be the value from
            the incoming dictionary in the BaseValidator class, similar to how
            it's done in Django with Models.

        """
        declared_fields = []
        required_fields = []

        for key, val in list(attrs.items()):
            if isinstance(val, Field):
                if val.required:
                    required_fields.append((key, val))
                declared_fields.append((key, val))
                attrs.pop(key)

        # Attach collected lists to attrs before object creation.
        attrs['fields'] = OrderedDict(declared_fields)
        attrs['required_fields'] = OrderedDict(required_fields)

        new_class = super().__new__(mcs, name, bases, attrs)
        return new_class


class Field:
    """ Validation Field. """

    def __init__(self, data_type: type = None,
                 validators: list = [],
                 required: bool = False) -> None:
        self.data_type = data_type
        self.validators = validators
        self.required = required

    def validate_type(self, val: Any):
        """ Validates field data type

        :param val: Value passed for checking
        :type val: Any

        :return: error message if any
        """
        err = None

        # A single valid data type
        if (type(self.data_type) != list) and (type(val) != self.data_type):
            formatted = FORMATTED_TYPE_NAMES[self.data_type.__name__]
            err = "'{}' is expected to be a '{}'".format(val,
                                                         formatted)

        # Multiple valid types are passed as a list
        elif (type(self.data_type) == list) and (type(val) not in self.data_type):
               error_msg = " or ".join([FORMATTED_TYPE_NAMES[t.__name__] for t in self.data_type])
               err = "'{}' is expected to be a '{}'".format(val, error_msg)

        return err

    def validate(self, val: Any) -> list:
        """ Validates value by passing into all validators

        :param val: Value to pass into validators
        :type val: Any

        :return: Errors or empty list.
        :rtype: list
        """
        errors: list = []

        if self.data_type:
            err_msg = self.validate_type(val)

            if err_msg:	# There was an error
                errors.append(err_msg)
                return errors

        for validator in self.validators:
            passed, err = validator(val)

            if not passed:
                errors.append(err)

        return errors
