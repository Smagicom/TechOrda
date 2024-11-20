#!/bin/bash

# Скачать архив и распаковать
curl -o jusan-dockerfile.zip https://stepik.org/media/attachments/lesson/686238/jusan-dockerfile.zip
unzip jusan-dockerfile.zip -d jusan-files

# Скачать архив и распаковать конф
curl -O https://stepik.org/media/attachments/lesson/686238/jusan-dockerfile.conf
docker build -t nginx:jusan-dockerfile .

./tester-dockerfile.sh 

