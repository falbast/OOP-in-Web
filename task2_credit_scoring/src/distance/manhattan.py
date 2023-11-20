from typing import Iterable

from distance.base import BaseSampleDistance


class ManhattanDistance(BaseSampleDistance):
    """Класс для определения расстояния между семплами (Манхэттеновское расстояние)."""

    k = 1

    @staticmethod
    def reduction(values: Iterable[float]) -> float:
        return sum(values)
