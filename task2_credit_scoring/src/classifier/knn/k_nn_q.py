import heapq

from collections import Counter

from classifier.knn.base import BaseKNNClassifier
from sample.base import BaseSample
from sample.train import TrainSample


class KNNQClassifier(BaseKNNClassifier):
    def classify(self, sample: BaseSample) -> bool:
        distances: list[tuple[float, TrainSample]] = [
            (self.distance.distance(sample, train), train) for train in self.train_data
        ]
        k_nearest = heapq.nsmallest(self.k, [train.status for d, train in distances])
        frequency: Counter[bool] = Counter(k_nearest)
        return frequency.most_common(1)[0][0]
