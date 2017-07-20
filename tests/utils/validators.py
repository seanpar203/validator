from validator import Validator, Field

from .validator_functions import TestValidators


class UserValidator(Validator):
    """
    User Test validator.
    """
    email = Field(
        data_type=str,
        validators=[TestValidators.is_email],
        required=True
    )
    age = Field(
        data_type=int,
        validators=[TestValidators.is_gt_than(10)]
    )
    height = Field(
        data_type=int,
        validators=[TestValidators.is_gt_but_lt(50, 90)]
    )
