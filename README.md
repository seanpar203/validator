## Validator
A simple way to validate dictionary values by using functions.


# Usage
There are 2 main classes to create custom validation classes(`Field`, `Validator`).

This is the simplest way to create a custom validator.
 
```python
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
  
```