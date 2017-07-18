import copy
from collections import defaultdict

from typing import Any

from validator.fields import Field, DeclarativeFieldsMetaclass


class BaseValidator:
	""" Base validation class, handles all logic. """

	def __init__(self, data: dict) -> None:
		self.data = data
		self._errors = None
		self.fields = copy.deepcopy(self.declared_fields)

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

	def full_validate(self):
		""" Runs full validation against all defined Fields.

		:return:
		"""
		self._errors = defaultdict(list)

		for key, val in self.data.items():
			try:
				field = self.fields[key]
			except KeyError:
				continue
			else:
				self._validate_field(field, key, val)

	# ------------------------------------------
	# Private Methods
	# ------------------------------------------

	def _validate_field(self, field: Field, key: str, val: Any) -> None:
		""" Validates a field by running value through validators.

		:param field: The validator field
		:type field: Field

		:param key: The key value for data & field.
		:type key: str

		:param val: The value of the data to pass into validators.
		:type val: Any
		"""
		for validator in field.validators:
			passed, err = validator(val)

			if not passed:
				self._errors[key].append(err)


class Validator(BaseValidator, metaclass=DeclarativeFieldsMetaclass):
	""" Class used to define custom Validator classes. """
	pass
