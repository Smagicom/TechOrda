#!/usr/bin/env bash
set -euo pipefail

is_container_present() {
    NLINES=$(docker ps -qa -f "name=jusan-dockerize" -f "status=running" -f "ancestor=jusan-fastapi-final:dockerized" | wc -l | sed "s/[[:space:]]//g")
    echo $NLINES
}

get_host_port() {
    HOST_PORT=$(docker container inspect jusan-dockerize | jq --raw-output '.[0]."HostConfig"."PortBindings"."8080/tcp"[0]."HostPort"')
    echo $HOST_PORT
}

is_port8080_present() {
    docker container inspect jusan-dockerize | grep "\"8080/tcp\": \[" > /dev/null
    echo $?
}

test_request() {
    RESP="$(echo $1 | jq --raw-output '.result')"
    if [ $RESP = $2 ] 
    then echo ✅ 
    else echo -e "❌ неправильный ответ от контейнера: $RESP\n$1" && exit 1 
    fi
}

if [ $(is_container_present) -eq 1 ] ; then echo ✅ ; else echo "❌ контейнер не найден" && exit 1 ; fi
if [ $(get_host_port) -eq 8080 ] ; then echo ✅ ; else echo "❌ неправильный порт хоста: $(get_host_port)" && exit 1 ; fi
if [ $(is_port8080_present) -eq 0 ] ; then echo ✅ ; else echo "❌ неправильный порт контейнера" && exit 1 ; fi

test_request "$(curl -s http://localhost:8080/sum1n/10)" 55
test_request "$(curl -s http://localhost:8080/fibo\?n=10)" 34
test_request "$(curl -s -X POST -H "string: hello" http://localhost:8080/reverse)" "olleh"
test_request "$(curl -s -H "Content-Type: application/json" -X POST -d '{"expr": "1,+,1"}' http://localhost:8080/calculator)" 2
