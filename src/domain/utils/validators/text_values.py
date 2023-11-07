from typing import Any


class TextValue:  # pylint: disable=R0903
    "Custom attribute descriptor to validate text values"

    field_name: str

    def __init__(self, min_length: int, max_length: int) -> None:
        self._min_length = min_length
        self._max_length = max_length

    def __set__(self, instance: Any, value: str):
        if not isinstance(value, str):
            raise AttributeError(f"Value of {self.field_name.upper()} is not a string")

        if len(value) < self._min_length or len(value) > self._max_length:
            raise AttributeError(
                f"Value '{value}' in {self.field_name.upper()} \
                    field is not in the range, should be between \
                        {self._min_length} and {self._max_length}"
            )

        instance.__dict__[self.field_name] = value

    def __set_name__(self, owner: Any, field_name: str) -> None:
        self.field_name = field_name
