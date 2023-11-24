from enum import Enum
from typing import Any, Self
from pydantic import BaseModel

from exceptions import InvalidSampleError


class HomeType(int, Enum):
    RENT = 1
    OWNER = 2
    PRIVATE = 3
    IGNORE = 4
    PARENTS = 5
    OTHER = 6


class MaritalType(int, Enum):
    SINGLE = 1
    MARRIED = 2
    WIDOW = 3
    SEPARATED = 4
    DIVORCED = 5


class JobType(int, Enum):
    FIXED = 1
    PART_TIME = 2
    FREELANCE = 3
    OTHERS = 4


class BaseSample(BaseModel):
    seniority: int
    home: HomeType
    time: int
    age: int
    marital: MaritalType
    records: bool
    job: JobType
    expenses: float
    income: float
    assets: float
    debt: float
    amount: float
    price: float

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({', '.join(f'{k}={v}' for k, v in self.__dict__.items())})"

    __str__ = __repr__

    @classmethod
    def from_dict(cls, row: dict[str, Any]) -> Self:
        try:
            return cls(**row)
        except ValueError as ex:
            raise InvalidSampleError(f"invalid {row!r}") from ex
