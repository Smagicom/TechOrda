# Используем Python как базовый образ
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY . /app

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт для работы API
EXPOSE 8000

# Запускаем приложение
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
