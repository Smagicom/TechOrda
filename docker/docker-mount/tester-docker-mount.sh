#!/usr/bin/env bash
set -euo pipefail

is_container_present() {
    NLINES=$(docker ps -qa -f "name=jusan-docker-mount" -f "status=running" -f "ancestor=nginx:mainline" | wc -l | sed "s/[[:space:]]//g")
    echo $NLINES
}

get_host_port() {
    HOST_PORT=$(docker container inspect jusan-docker-mount | jq --raw-output '.[0]."HostConfig"."PortBindings"."80/tcp"[0]."HostPort"')
    echo $HOST_PORT
}

is_port80_present() {
    docker container inspect jusan-docker-mount | grep "\"80/tcp\": \[" > /dev/null
    echo $?
}

request() {
    curl -H "Host: example.com" -s $1 | awk 'NF'
}

if [ $(is_container_present) -eq 1 ] ; then echo ✅ ; else echo "❌ контейнер не найден" && exit 1 ; fi
if [ $(get_host_port) -eq 9999 ] ; then echo ✅ ; else echo "❌ неправильный порт хоста: $(get_host_port)" && exit 1 ; fi
if [ $(is_port80_present) -eq 0 ] ; then echo ✅ ; else echo "❌ неправильный порт контейнера" && exit 1 ; fi
if [ "$(request http://localhost:9999)" = '<h1>Hello, from jusan-docker-mount</h1>' ] ; then echo ✅ ; else echo "❌ неправильный ответ от контейнера: localhost:9999/" && exit 1 ; fi
if [ "$(request http://localhost:9999/test)" = 'Singularity' ] ; then echo ✅ ; else echo "❌ неправильный ответ от контейнера: localhost:9999/test" && exit 1 ; fi
if [ "$(request http://localhost:9999/token)" = 'Jusan' ] ; then echo ✅ ; else echo "❌ неправильный ответ от контейнера: localhost:9999/token" && exit 1 ; fi
