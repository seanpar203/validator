Validator
=========
|PyPI| |PyPI version|

A simple way to validate dictionary values by using functions.


Installation
------------
- ``pip3 install simple-validator``


Usage
-----
There are 2 main classes to create custom validation classes(``Field``, ``Validator``).

.. code:: python

    from validator import Field, Validator


    def is_valid_email(val: str):
        """ A horrible way to check if a string is a valid email. """
        passed = False
        err_msg = "{} isn't a valid email.".format(val)

        if '@' in val:
            passed = True
        return passed, err_msg


    class UserValidator(Validator):
        """ Validates a user dictionary. """
        email = Field(data_type=str, validators=[is_valid_email])


Validation
----------
The Validator provides the same api as Django forms for checking if all the fields
are valid.

.. code:: python

    data = {
        'email': 'Sean@parsons.com'
    }

    user = UserValidator(data)

    if user.is_valid():
        # Do things in here...
        email = user.email # Optionally you can do user.data['email']
    else:
        print(user.errors)

Errors
------
The ``Validator.errors`` attribute is a ``defaultdict(list)``.

When validators don't pass, the declared field(Ex: 'email', 'password' etc..) errors gets populated with the return error string from the validator.

.. code:: python

    data = {
        'email': 'sean'
    }

    user = UserValidator(data)

    if user.is_valid():
        # Do things in here...
    else:
        print(user.errors['email'])

        # "sean isn't a valid email."


Validating Field Types
----------------------
The ``Field`` class has a ``data_type`` parameter which should be used to validate a field value
before passing it into validators.

This prevents from having ``try, except, else`` blocks inside of validator functions because your guaranteed
it won't be passed into validators until it's the correct type.

**If the field value is the wrong type, it will ony return an error like the one below**


.. code:: python

    data = {
        'email': 1
    }

    user = UserValidator(data)

    if user.is_valid():
        # Do things in here...
    else:
        print(user.errors['email'])

        # "'1' is expected to be a 'String'"


.. |PyPI| image:: https://img.shields.io/pypi/v/simple-validator.svg
   :target: https://pypi.python.org/pypi/simple-validator/

.. |PyPI version| image:: https://img.shields.io/pypi/pyversions/simple-validator.svg
   :target: https://pypi.python.org/pypi/simple-validator/
