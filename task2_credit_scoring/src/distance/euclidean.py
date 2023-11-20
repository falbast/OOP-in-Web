from typing import Iterable

from distance.base import BaseSampleDistance


class EuclideanDistance(BaseSampleDistance):
    """Класс для определения расстояния между семплами (Евклидово расстояние)"""

    k = 2

    @staticmethod
    def reduction(values: Iterable[float]) -> float:
        return sum(values)
