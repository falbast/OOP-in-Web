import random
import pytest

from classifier.knn.k_nn import KNNClassifier
from classifier.knn.k_nn_q import KNNQClassifier
from distance.chebyshev import ChebyshevDistance
from distance.euclidean import EuclideanDistance
from distance.manhattan import ManhattanDistance
from distance.sorensen import SorensenDistance
from exceptions import InvalidSampleError
from hyperparameter import Hyperparameter
from sample.base import BaseSample, MaritalType, HomeType, JobType
from sample.classified import ClassifiedSample
from sample.known import KnownSample
from sample.test import TestSample
from sample.train import TrainSample
from sample.unknown import UnknownSample
from training_data import TrainingData


random.seed(0)

TEST_SAMPLES = [
    {
        "seniority": random.randint(0, 30),
        "home": random.choice([x for x in HomeType]),
        "time": random.randint(1, 60),
        "age": random.randint(18, 90),
        "marital": random.choice([x for x in MaritalType]),
        "records": random.choice([True, False]),
        "job": random.choice([x for x in JobType]),
        "expenses": random.randint(0, 9999999),
        "income": random.randint(0, 9999999),
        "assets": random.randint(0, 99999999),
        "debt": random.randint(0, 999999),
        "amount": random.randint(0, 999999),
        "price": random.randint(0, 999999),
    }
    for _ in range(25)
]

TEST_SAMPLE_DATA = TEST_SAMPLES[0]


def test_distances() -> None:
    base_sample_1 = BaseSample.from_dict(TEST_SAMPLE_DATA)
    base_sample_2 = BaseSample.from_dict(TEST_SAMPLE_DATA)
    assert ChebyshevDistance().distance(base_sample_1, base_sample_2) == 0.0
    assert EuclideanDistance().distance(base_sample_1, base_sample_2) == 0.0
    assert ManhattanDistance().distance(base_sample_1, base_sample_2) == 0.0
    assert SorensenDistance().distance(base_sample_1, base_sample_2) == 0.0

    changed_test_sample_data = TEST_SAMPLE_DATA
    changed_test_sample_data["age"] = 20

    base_sample_3 = BaseSample.from_dict(changed_test_sample_data)
    assert ChebyshevDistance().distance(base_sample_1, base_sample_3) != 0.0
    assert EuclideanDistance().distance(base_sample_1, base_sample_3) != 0.0
    assert ManhattanDistance().distance(base_sample_1, base_sample_3) != 0.0
    assert SorensenDistance().distance(base_sample_1, base_sample_3) != 0.0


def test_samples() -> None:
    base_sample = BaseSample.from_dict(TEST_SAMPLE_DATA)
    print(base_sample)
    unknown_sample = UnknownSample.from_dict(TEST_SAMPLE_DATA)
    print(unknown_sample)
    known_sample = KnownSample.from_dict(TEST_SAMPLE_DATA | {"status": True})
    print(known_sample)
    classified_sample = ClassifiedSample.from_dict(
        unknown_sample.dict() | {"predict": True}
    )
    print(classified_sample)
    train_sample = TrainSample.from_dict(TEST_SAMPLE_DATA | {"status": True})
    print(train_sample)
    test_sample = TestSample.from_dict(
        TEST_SAMPLE_DATA | {"predict": True, "status": True}
    )
    assert test_sample.is_predict_correct is True
    test_sample_without_predict = TestSample.from_dict(
        TEST_SAMPLE_DATA | {"status": True}
    )
    with pytest.raises(AttributeError):
        print(test_sample_without_predict.is_predict_correct)


def test_training_data() -> None:
    some_training_data = TrainingData(name="train")
    some_training_data.load(
        raw_rows=[sample | {"age": "wrongage"} for sample in TEST_SAMPLES]
    )
    some_training_data.load(
        raw_rows=[
            sample | {"status": random.choice([True, False])} for sample in TEST_SAMPLES
        ]
    )
    for classifier_class in [KNNClassifier, KNNQClassifier]:
        for distance_class in [
            ChebyshevDistance,
            EuclideanDistance,
            ManhattanDistance,
            SorensenDistance,
        ]:
            for k in range(1, 10):
                classifier = classifier_class(
                    k=k,
                    distance=distance_class(),  # type: ignore
                    train_data=some_training_data.training,
                )
                h = Hyperparameter(classifier=classifier)
                some_training_data.test(h)
                print(
                    f"{k=}; {distance_class.__name__=}; {classifier_class.__name__=}; {h.quality=}"
                )
                random_sample = UnknownSample.from_dict(random.choice(TEST_SAMPLES))
                print(
                    f"Random classify: {some_training_data.classify(h, random_sample)}"
                )
    with pytest.raises(InvalidSampleError):
        UnknownSample.from_dict(random.choice(TEST_SAMPLES) | {"age": "someage"})


def main() -> None:
    test_samples()
    test_distances()
    test_training_data()


if __name__ == "__main__":
    main()
