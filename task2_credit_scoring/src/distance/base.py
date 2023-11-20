from abc import ABC, abstractmethod
from typing import Iterable, Any

from exceptions import InvalidCoefficientValue
from sample.base import BaseSample


class BaseDistance(ABC):
    """Базовый класс для определения формулы расстояния."""

    @abstractmethod
    def distance(self, s1: Any, s2: Any) -> float:
        ...


class BaseSampleDistance(BaseDistance):
    """Базовый класс для определения формулы расстояния между семплами."""

    @property
    @abstractmethod
    def k(self) -> int:
        ...

    @staticmethod
    @abstractmethod
    def reduction(values: Iterable[float]) -> float:
        ...

    def distance(self, s1: BaseSample, s2: BaseSample) -> float:
        if self.k == 0:
            raise InvalidCoefficientValue
        return float(
            self.reduction(
                [
                    abs(s1.seniority - s2.seniority) ** self.k,
                    abs(s1.home - s2.home) ** self.k,
                    abs(s1.time - s2.time) ** self.k,
                    abs(s1.age - s2.age) ** self.k,
                    abs(s1.marital - s2.marital) ** self.k,
                    abs(s1.records - s2.records) ** self.k,
                    abs(s1.job - s2.job) ** self.k,
                    abs(s1.expenses - s2.expenses) ** self.k,
                    abs(s1.income - s2.income) ** self.k,
                    abs(s1.assets - s2.assets) ** self.k,
                    abs(s1.debt - s2.debt) ** self.k,
                    abs(s1.amount - s2.amount) ** self.k,
                    abs(s1.price - s2.price) ** self.k,
                ]
            )
            ** (1 / self.k)
        )
