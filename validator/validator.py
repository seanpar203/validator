from typing import DefaultDict
from collections import defaultdict
from validator.fields import Field, DeclarativeFieldsMetaclass


class BaseValidator:
    """ Base validation class, handles all logic. """

    def __init__(self, data: dict) -> None:
        self.data = data
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
