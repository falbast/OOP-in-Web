# Bumbo: Python Web Framework built for learning purposes
- Подготовка к работе:
1. Смена директории
```cmd
cd "C:\Users\Random\Desktop\OOP_python\task3_framework\framework\webapp"
```

2. Создание виртуального окружения:
```cmd
C:\Users\Random\AppData\Local\Programs\Python\Python37-32\python -m venv venv
```

3. Активация виртуального окружения
```
venv\Scripts\activate.bat
```

4. Установка WSGI Web-сервер (Используем Waitress вместо GUnicorn, так как используемая ОС - Windows)
```cmd
pip install waitress
```

#
- Запуск Web-приложения:
Запуск Waitress
```cmd
waitress-serve --listen=127.0.0.1:8000 app:app
```