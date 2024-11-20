#!/bin/bash

# Запуск контейнера с указанными параметрами
docker run -d \
  --name jusan-docker-bind \
  -p 7777:80 \
  -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf:ro \
  nginx:mainline

# Проверка доступности сервера
curl http://localhost:7777

# Показ списка запущенных контейнеров
docker ps

# Вывод логов nginx
docker logs jusan-docker-bind

