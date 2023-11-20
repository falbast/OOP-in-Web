from src.distance.base import BaseDistance
from src.sample.base import BaseSample


class SorensenDistance(BaseDistance):
    """Класс для определения расстояния между семплами (Расстояние Соренсена)"""

    def distance(self, s1: BaseSample, s2: BaseSample) -> float:
        return sum(
            [
                abs(s1.seniority - s2.seniority),
                abs(s1.home - s2.home),
                abs(s1.time - s2.time),
                abs(s1.age - s2.age),
                abs(s1.marital - s2.marital),
                abs(s1.records - s2.records),
                abs(s1.job - s2.job),
                abs(s1.expenses - s2.expenses),
                abs(s1.income - s2.income),
                abs(s1.assets - s2.assets),
                abs(s1.debt - s2.debt),
                abs(s1.amount - s2.amount),
                abs(s1.price - s2.price),
            ]
        ) / sum(
            [
                abs(s1.seniority + s2.seniority),
                abs(s1.home + s2.home),
                abs(s1.time + s2.time),
                abs(s1.age + s2.age),
                abs(s1.marital + s2.marital),
                abs(s1.records + s2.records),
                abs(s1.job + s2.job),
                abs(s1.expenses + s2.expenses),
                abs(s1.income + s2.income),
                abs(s1.assets + s2.assets),
                abs(s1.debt + s2.debt),
                abs(s1.amount + s2.amount),
                abs(s1.price + s2.price),
            ]
        )
