#!/bin/bash

# Запуск контейнера с указанными параметрами
docker run -d \
  --name jusan-docker-mount \
  -p 9999:80 \
  -v $(pwd)/jusan-docker-mount.conf:/etc/nginx/conf.d/jusan-docker-mount.conf:ro \
  -v $(pwd)/jusan-docker-mount:/usr/share/nginx/html:ro \
  nginx:mainline

# Проверка запросов
curl http://localhost:9999
curl http://localhost:9999/test
curl http://localhost:9999/token

# Просмотр логов
docker logs jusan-docker-mount
