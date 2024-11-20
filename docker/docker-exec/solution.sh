#!/bin/bash

# Запуск контейнера
docker run -d \
  --name jusan-docker-exec \
  -p 8181:80 \
  nginx:mainline

# Вход в контейнер и создание нового конфигурационного файла
docker exec -it jusan-docker-exec bash -c "cat << EOF > /etc/nginx/conf.d/jusan-docker-exec.conf
server {
    listen 80;
    server_name jusan.singularity;

    location / {return 200 'Hello, from jusan-docker-exec';}
    location /home {return 201 'This is my home!';}
    location /about {return 202 'I am just an exercise!';}
}
EOF"

# Перезагрузка nginx внутри контейнера
docker exec jusan-docker-exec nginx -s reload

# Проверка запросов с помощью curl
curl http://localhost:8181
curl http://localhost:8181/home
curl http://localhost:8181/about

# Просмотр логов nginx
docker logs jusan-docker-exec
