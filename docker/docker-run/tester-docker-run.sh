#!/usr/bin/env bash
set -euo pipefail

is_container_present() {
    NLINES=$(docker ps -qa -f "name=jsn-dkr-run" -f "status=exited" -f "ancestor=nginx:mainline" | wc -l | sed "s/[[:space:]]//g")
    echo $NLINES
}

get_host_port() {
    HOST_PORT=$(docker container inspect jsn-dkr-run | jq --raw-output '.[0]."HostConfig"."PortBindings"."80/tcp"[0]."HostPort"')
    echo $HOST_PORT
}

is_port80_present() {
    docker container inspect jsn-dkr-run | grep "\"80/tcp\": \[" > /dev/null
    echo $?
}

if [ $(is_container_present) -eq 1 ] ; then echo ✅ ; else echo "❌ контейнер не найден" && exit 1 ; fi
if [ $(get_host_port) -eq 8888 ] ; then echo ✅ ; else echo "❌ неправильный порт хоста: $(get_host_port)" && exit 1 ; fi
if [ $(is_port80_present) -eq 0 ] ; then echo ✅ ; else echo "❌ неправильный порт контейнера" && exit 1 ; fi
