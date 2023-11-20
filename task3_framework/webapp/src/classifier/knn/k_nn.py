from collections import Counter

from src.classifier.knn.base import BaseKNNClassifier
from src.sample.base import BaseSample
from src.sample.train import TrainSample


class KNNClassifier(BaseKNNClassifier):
    def classify(self, sample: BaseSample) -> bool:
        distances: list[tuple[float, TrainSample]] = [
            (self.distance.distance(sample, train), train) for train in self.train_data
        ]
        k_nearest = (train.status for d, train in distances[: self.k])
        frequency: Counter[bool] = Counter(k_nearest)
        return frequency.most_common(1)[0][0]
