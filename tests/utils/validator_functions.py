from typing import Callable, Tuple, Dict, Any

# Constant Type.
validator_tuple = Tuple[bool, str]


class TestValidators:
    """ Utility class for storing validators that return False. """

    @staticmethod
    def is_email(val: str) -> validator_tuple:
        passed = False
        err = f"{val} must contain @"

        if '@' in val:
            passed = True

        return passed, err

    @staticmethod
    def is_secure_password(val: str) -> validator_tuple:
        passed: bool = False
        err: str = "Password must be at least 8 characters in length and alphanumeric"

        if len(val) >= 8 and val.isalnum():
            passed = True

        return passed, err

    @staticmethod
    def is_min_length(min_length: int) -> Callable[[str], validator_tuple]:
        def validator(val: str) -> validator_tuple:
            passed: bool = False
            err: str = f"{val} must be at least {min_length} characters in length"

            if len(val) >= min_length:
                passed = True

            return passed, err

        return validator

    @staticmethod
    def is_gt_than(num: int) -> Callable[[int], validator_tuple]:
        def validator(val: int) -> validator_tuple:
            passed: bool = False
            err: str = f"{val} must be larger than {num}"

            if val > num:
                passed = True

            return passed, err

        return validator

    @staticmethod
    def is_gt_but_lt(flr: int, ceil: int) -> Callable[[int], validator_tuple]:
        def validator(val: int) -> validator_tuple:
            passed: bool = False
            err: str = f"{val} must be greater than {flr} and less than {ceil}"

            if flr < val < ceil:
                passed = True

            return passed, err

        return validator
