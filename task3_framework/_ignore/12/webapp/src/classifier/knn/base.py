from abc import abstractmethod

from src.classifier.base import BaseSampleClassifier
from src.distance.base import BaseDistance
from src.sample.base import BaseSample
from src.sample.train import TrainSample


class BaseKNNClassifier(BaseSampleClassifier):
    def __init__(self, k: int, distance: BaseDistance, train_data: list[TrainSample]):
        self.k = k
        self.distance = distance
        super().__init__(train_data=train_data)

    @abstractmethod
    def classify(self, s: BaseSample) -> bool:
        ...
