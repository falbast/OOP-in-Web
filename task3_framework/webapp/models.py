from typing import NamedTuple
from src.sample.base import HomeType, MaritalType, JobType

class WebSample(NamedTuple):
    id: int
    seniority: int
    home: HomeType
    time: int
    age: int
    marital: MaritalType
    records: bool
    job: JobType
    expenses: float
    income: float
    assets: float
    debt: float
    amount: float
    price: float
    predict: bool = None
