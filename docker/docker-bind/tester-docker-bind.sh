#!/usr/bin/env bash
set -euo pipefail

is_container_present() {
    NLINES=$(docker ps -qa -f "name=jusan-docker-bind" -f "status=running" -f "ancestor=nginx:mainline" | wc -l | sed "s/[[:space:]]//g")
    echo $NLINES
}

get_host_port() {
    HOST_PORT=$(docker container inspect jusan-docker-bind | jq --raw-output '.[0]."HostConfig"."PortBindings"."80/tcp"[0]."HostPort"')
    echo $HOST_PORT
}

is_port80_present() {
    docker container inspect jusan-docker-bind | grep "\"80/tcp\": \[" > /dev/null
    echo $?
}

get_resp() {
    RESP=$(curl -s http://localhost:7777)
    echo $RESP | awk 'NF'
}

if [ $(is_container_present) -eq 1 ] ; then echo ✅ ; else echo "❌ контейнер не найден" && exit 1 ; fi
if [ $(get_host_port) -eq 7777 ] ; then echo ✅ ; else echo "❌ неправильный порт хоста: $(get_host_port)" && exit 1 ; fi
if [ $(is_port80_present) -eq 0 ] ; then echo ✅ ; else echo "❌ неправильный порт контейнера" && exit 1 ; fi
if [ "$(get_resp)" = 'Привет из Docker контейнера! 🐳' ] ; then echo ✅ ; else echo "❌ неправильный ответ от контейнера" && exit 1 ; fi
