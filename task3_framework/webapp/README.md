# Model
Установка зависимостей:

`pip install -r requirements.txt`

Проверка типизации:

`mypy --strict --show-error-codes src`

Проверка тестов:

`cd src && python -m pytest tests.py`


# Web App
- Подготовка к работе:
Смена директории
```cmd
cd project_directory
```

Создание виртуального окружения:
```cmd
python3 -m venv venv
```

Активация виртуального окружения
```cmd
venv/Scripts/activate.bat
```

Установка WSGI Web-сервер (Используем Waitress вместо GUnicorn, так как используемая ОС - Windows)
```cmd
pip install waitress
```

- Запуск Web-приложения:
Запуск Waitress
```cmd
waitress-serve --listen=127.0.0.1:8000 app:app
```
