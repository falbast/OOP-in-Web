import random
import pandas as pd

from models import WebSample
from src.sample.base import HomeType, MaritalType, JobType
from src.classifier.knn.k_nn_q import KNNQClassifier
from src.distance.manhattan import ManhattanDistance
from src.hyperparameter import Hyperparameter
from src.sample.unknown import UnknownSample
from src.training_data import TrainingData


df = pd.read_csv('data\data.csv', usecols=['Status', 'Seniority', 'Home', 'Time', 'Age', 'Marital', 'Records', 'Job', 'Expenses', 'Income', 'Assets', 'Debt', 'Amount', 'Price'])
DATA_SAMPLES = df.to_dict(orient='records')


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
        #kwargs["predict"] = False
        some_training_data = TrainingData(name="train")
        some_training_data.load(raw_rows=[sample for sample in DATA_SAMPLES])
        print(some_training_data.training)
        print(some_training_data)
        print(kwargs)
        classifier = KNNQClassifier(
            k=5,
            distance=ManhattanDistance(),  # type: ignore
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

def main() -> None:
    sample_storage = SampleStorage()
    sample_storage.create(
            seniority=random.randint(0, 30), 
            home=random.choice([x.value for x in HomeType]), 
            time=random.randint(1, 60), 
            age=random.randint(18, 90), 
            marital=random.choice([x.value for x in MaritalType]), 
            records=random.choice([True, False]), 
            job=random.choice([x.value for x in JobType]), 
            expenses=random.randint(0, 9999999), 
            income=random.randint(0, 9999999), 
            assets=random.randint(0, 99999999), 
            debt=random.randint(0, 999999), 
            amount=random.randint(0, 999999), 
            price=random.randint(0, 999999)
    )

if __name__ == "__main__":
    main()