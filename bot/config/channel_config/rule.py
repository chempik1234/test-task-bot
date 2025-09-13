from typing import Any, TypeVar, Generic, List

T = TypeVar('T')


class Rule:
    field: str
    filter: Any

    def __init__(self, field: str, filter: Any):
        self.field = field
        self.filter = filter

    def check(self, value: str) -> bool:
        """
        check if a record satisfies given rule
        :param value: value to check
        :return: bool value of whether the record satisfies given rule or not
        """
        raise NotImplementedError()

    def to_kwarg(self):
        raise NotImplementedError()


class OneOfListRule(Rule, Generic[T]):
    field: T
    filter: List[T]

    def __init__(self, field: T, filter: List[T]):
        super().__init__(field, filter)

    def check(self, value: str) -> bool:
        return value in self.filter

    def to_kwarg(self):
        return f"{self.field}__in", self.filter
