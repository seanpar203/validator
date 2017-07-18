from collections import OrderedDict


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
		attrs['declared_fields'] = OrderedDict(current_fields)

		new_class = super().__new__(mcs, name, bases, attrs)
		return new_class


class Field:
	""" Validation Field. """

	def __init__(self, validators: tuple = ()) -> None:
		self.validators = validators
