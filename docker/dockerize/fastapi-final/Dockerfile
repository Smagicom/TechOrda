# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем все файлы в рабочую директорию контейнера
COPY . /app

# Устанавливаем зависимости из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт 8080
EXPOSE 8080

# Команда для запуска FastAPI приложения (проверьте путь к вашему файлу, если нужно)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

