import random

from models import WebSample
from src.sample.base import HomeType, MaritalType, JobType
from src.classifier.knn.k_nn import KNNClassifier
from src.distance.manhattan import ManhattanDistance
from src.hyperparameter import Hyperparameter
from src.sample.unknown import UnknownSample
from src.training_data import TrainingData


DATA_SAMPLES = [
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
    for _ in range(100)
]


class SampleStorage:
    _id = 0

    def __init__(self):
        self._samples = []

    def all(self):
        return [sample._asdict() for sample in self._samples]

    def get(self, id: int):
        for sample in self._samples:
            if sample.id == id:
                return sample

        return None


    def create(self, **kwargs):
        self._id += 1
        kwargs["id"] = self._id
        
        some_training_data = TrainingData(name="train")
        some_training_data.load(
            raw_rows=[
                sample | {"status": random.choice([True, False])} for sample in DATA_SAMPLES
            ]
        )
        classifier = KNNClassifier(
            k=5,
            distance=ManhattanDistance(),
            train_data=some_training_data.training,
        )
        h = Hyperparameter(classifier=classifier)
        some_training_data.test(h)
        random_sample = UnknownSample.from_dict(random.choice(DATA_SAMPLES))
        classified_sample = some_training_data.classify(h, random_sample)
        
        kwargs["predict"] = classified_sample.predict
        sample = WebSample(**kwargs)
        self._samples.append(sample)
        
        return sample

    def delete(self, id):
        for ind, sample in enumerate(self._samples):
            if sample.id == id:
                del self._samples[ind]
