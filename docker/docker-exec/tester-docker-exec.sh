#!/usr/bin/env bash
set -euo pipefail

is_container_present() {
    NLINES=$(docker ps -qa -f "name=jusan-docker-exec" -f "status=running" -f "ancestor=nginx:mainline" | wc -l | sed "s/[[:space:]]//g")
    echo $NLINES
}

get_host_port() {
    HOST_PORT=$(docker container inspect jusan-docker-exec | jq --raw-output '.[0]."HostConfig"."PortBindings"."80/tcp"[0]."HostPort"')
    echo $HOST_PORT
}

is_port80_present() {
    docker container inspect jusan-docker-exec | grep "\"80/tcp\": \[" > /dev/null
    echo $?
}

request() {
    curl -H "Host: jusan.singularity" -s $1 | awk 'NF'
}

if [ $(is_container_present) -eq 1 ] ; then echo ✅ ; else echo "❌ контейнер не найден" && exit 1 ; fi
if [ $(get_host_port) -eq 8181 ] ; then echo ✅ ; else echo "❌ неправильный порт хоста: $(get_host_port)" && exit 1 ; fi
if [ $(is_port80_present) -eq 0 ] ; then echo ✅ ; else echo "❌ неправильный порт контейнера" && exit 1 ; fi
if [ "$(request http://localhost:8181)" = 'Hello, from jusan-docker-exec' ] ; then echo ✅ ; else echo "❌ неправильный ответ от контейнера: localhost:8181/" && exit 1 ; fi
if [ "$(request http://localhost:8181/home)" = 'This is my home!' ] ; then echo ✅ ; else echo "❌ неправильный ответ от контейнера: localhost:8181/home" && exit 1 ; fi
if [ "$(request http://localhost:8181/about)" = 'I am just an exercise!' ] ; then echo ✅ ; else echo "❌ неправильный ответ от контейнера: localhost:8181/about" && exit 1 ; fi