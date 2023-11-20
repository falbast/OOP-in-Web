from models import WebSample


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
        sample = WebSample(**kwargs)
        self._samples.append(sample)
        return sample

    def delete(self, id):
        for ind, sample in enumerate(self._samples):
            if sample.id == id:
                del self._samples[ind]
