from typing import Any


def duplicate_value(value: Any):
    return value + value


def duplicate_str_value(value: str):
    if not isinstance(value, str):
        raise TypeError("Expected str")
    return value + value
