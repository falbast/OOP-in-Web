from sample.known import KnownSample


class TestSample(KnownSample):
    """Тестовые данные. Классификатор присваивает класс, который может быть корректным или некорректным."""

    predict: bool | None = None

    @property
    def is_predict_correct(self) -> bool:
        if self.predict is None:
            raise AttributeError("No predicted value")
        return self.status == self.predict
