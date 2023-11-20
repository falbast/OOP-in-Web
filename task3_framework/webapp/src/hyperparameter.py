from src.classifier.base import BaseSampleClassifier
from src.sample.test import TestSample
from src.sample.unknown import UnknownSample


class Hyperparameter:
    def __init__(self, classifier: BaseSampleClassifier):
        self.classifier = classifier
        self.quality: float | None = None

    def test(self, test_samples: list[TestSample]) -> float:
        """Запускает классификацию на тестовом наборе"""
        for sample in test_samples:
            sample.predict = self.classify(sample)
        self.quality = len(
            [sample for sample in test_samples if sample.is_predict_correct]
        ) / len(test_samples)
        return self.quality

    def classify(self, sample: UnknownSample | TestSample) -> bool:
        return self.classifier.classify(sample)
