from typing import DefaultDict
from collections import defaultdict
from validator.fields import Field, DeclarativeFieldsMetaclass


class BaseValidator:
    """ Base validation class, handles all logic. """

    def __init__(self, data: dict) -> None:
        self.data = data
        self._missing_fields: set = set()
        self._errors: DefaultDict[str, list] = defaultdict(list)

    # ------------------------------------------
    # Properties
    # ------------------------------------------

    @property
    def errors(self) -> defaultdict:
        """ Returns dictionary with or without errors.

        :return: Errors
        :rtype: defaultdict
        """
        if not self._errors:
            self.full_validate()
        return self._errors

    @property
    def missing_fields(self) -> set:
        """ Returns a set of the missing fields.

        :return: True or False
        :rtype: bool
        """
        if not self._missing_fields:
            self._missing_fields = (
                set(self.required_fields.keys()) - set(self.data.keys())
            )
        return self._missing_fields

    # ------------------------------------------
    # Public Methods
    # ------------------------------------------

    def is_valid(self) -> bool:
        """ Returns if there is errors in validation.

        :return: True or False
        :rtype: bool
        """
        return not self.errors

    def full_validate(self) -> None:
        """ Runs full validation against all defined Fields. """

        self._errors: DefaultDict[str, list] = defaultdict(list)

        # Add missing fields to part of errors
        # if there's missing fields.
        if self.missing_fields:
            for field in self.missing_fields:
                self._errors[field].append(
                    "{} field is required.".format(field)
                )

        # Pass values through validation
        # where this is a declared Field.
        for key, val in self.data.items():
            try:
                field: Field = self.fields[key]
            except KeyError:
                continue
            else:
                errors: list = field.validate(val)

                if errors:
                    self._errors[key].extend(errors)
            finally:
                setattr(self, key, val)


class Validator(BaseValidator, metaclass=DeclarativeFieldsMetaclass):
    """ Class used to define custom Validator classes. """
    pass
