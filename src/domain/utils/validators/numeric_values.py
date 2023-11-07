from typing import Any, Union, TypeAlias

Numeric: TypeAlias = Union[int, float]


class NumericValue:  # pylint: disable=R0903
    "Custom attribute descriptor to validate numeric values"

    field_name: str

    def __init__(self, min_value: int, max_value: int) -> None:
        self._min = min_value
        self._max = max_value

    def __set__(self, instance: Any, value: Numeric):
        if not isinstance(value, Numeric):  # type: ignore
            raise AttributeError(f"Value of {self.field_name.upper()} is not a numeric")

        if value < self._min or value > self._max:
            raise AttributeError(
                f"Value {value} in {self.field_name.upper()} \
                    field is not in the range, should be between \
                        {self._min} and {self._max}"
            )

        instance.__dict__[self.field_name] = value

    def __set_name__(self, owner: Any, field_name: str) -> None:
        self.field_name = field_name
