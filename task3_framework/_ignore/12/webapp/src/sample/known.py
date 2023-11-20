from src.sample.base import BaseSample


class KnownSample(BaseSample):
    """Абстрактный класс для тренировочных и тестовых данных, тип данных задается дополнительно."""

    status: bool
