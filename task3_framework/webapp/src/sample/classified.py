from src.sample.unknown import UnknownSample


class ClassifiedSample(UnknownSample):
    """Создается на основе образца, предоставленного пользователем, и результата классификации."""

    predict: bool
