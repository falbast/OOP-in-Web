Установка зависимостей:

`pip install -r requirements.txt`

Проверка линтером:

`black src`

Проверка типизации:

`mypy --strict --show-error-codes src`

Проверка тестов:

`cd src && python -m pytest tests.py`
