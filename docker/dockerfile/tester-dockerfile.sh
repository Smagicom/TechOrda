#!/usr/bin/env bash
set -euo pipefail

is_container_present() {
    NLINES=$(docker ps -qa -f "name=jusan-dockerfile" -f "status=running" -f "ancestor=nginx:jusan-dockerfile" | wc -l | sed "s/[[:space:]]//g")
    echo $NLINES
}

get_host_port() {
    HOST_PORT=$(docker container inspect jusan-dockerfile | jq --raw-output '.[0]."HostConfig"."PortBindings"."80/tcp"[0]."HostPort"')
    echo $HOST_PORT
}

is_port80_present() {
    docker container inspect jusan-dockerfile | grep "\"80/tcp\": \[" > /dev/null
    echo $?
}

request() {
    curl -H "Host: jusan.dockerfile" -s $1 | awk 'NF'
}

if [ $(is_container_present) -eq 1 ] ; then echo ✅ ; else echo "❌ контейнер не найден" && exit 1 ; fi
if [ $(get_host_port) -eq 6060 ] ; then echo ✅ ; else echo "❌ неправильный порт хоста: $(get_host_port)" && exit 1 ; fi
if [ $(is_port80_present) -eq 0 ] ; then echo ✅ ; else echo "❌ неправильный порт контейнера" && exit 1 ; fi
if [ "$(request http://localhost:6060)" = '<h1>Hello, from jusan-dockerfile!</h1>' ] ; then echo ✅ ; else echo "❌ неправильный ответ от контейнера: http://localhost:6060" && exit 1 ; fi
if [ "$(request http://localhost:6060/dockerfile)" = 'FROM nginx:mainline' ] ; then echo ✅ ; else echo "❌ неправильный ответ от контейнера: http://localhost:6060/dockerfile" && exit 1 ; fi
if [ "$(request http://localhost:6060/secret)" = 'jusan-dockerfile' ] ; then echo ✅ ; else echo "❌ неправильный ответ от контейнера: http://localhost:6060/secret" && exit 1 ; fi
if [ "$(request http://localhost:6060/jusan)" = 'singularity' ] ; then echo ✅ ; else echo "❌ неправильный ответ от контейнера: http://localhost:6060/jusan" && exit 1 ; fi
