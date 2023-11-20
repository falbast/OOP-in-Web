import datetime

from typing import Iterable, Any

from exceptions import InvalidSampleError
from hyperparameter import Hyperparameter
from sample.classified import ClassifiedSample
from sample.test import TestSample
from sample.train import TrainSample
from sample.unknown import UnknownSample


class TrainingData:
    """Набор обучающих и тестовых данных с методами для загрузки и тестирования образцов."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.uploaded: datetime.datetime | None = None
        self.tested: datetime.datetime | None = None
        self.training: list[TrainSample] = []
        self.testing: list[TestSample] = []
        self.tuning: list[Hyperparameter] = []

    def load(self, raw_rows: Iterable[dict[str, Any]]) -> None:
        """Извлекает TestSample и TrainSample из сырых данных и валидирует"""
        for n, row in enumerate(raw_rows):
            try:
                if n % 5 == 0:
                    self.testing.append(TestSample.from_dict(row))
                else:
                    self.training.append(TrainSample.from_dict(row))
            except InvalidSampleError as ex:
                print(f"Row {n + 1}: {ex}")
        self.uploaded = datetime.datetime.now(tz=datetime.timezone.utc)

    def test(self, h: Hyperparameter) -> None:
        """Проверка значения гиперпараметра."""
        h.test(test_samples=self.testing)
        self.tuning.append(h)
        self.tested = datetime.datetime.now(tz=datetime.timezone.utc)

    @staticmethod
    def classify(parameter: Hyperparameter, sample: UnknownSample) -> ClassifiedSample:
        return ClassifiedSample(predict=parameter.classify(sample), **sample.dict())
