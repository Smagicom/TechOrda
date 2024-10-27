#!/usr/bin/env bash

is_container_present() {
    # $1 - container name
    # $2 - container status
    # $3 - container image
    # echo's 1 if present, 0 if not

    NLINES=$(docker ps -qa -f "name=^$1\$" -f "status=$2" -f "ancestor=$3" | wc -l | sed "s/[[:space:]]//g")
    echo $NLINES
}

get_host_port() {
    # $1 - container name
    # $2 - container inner port
    # echo's host port

    HOST_PORT=$(docker container inspect $1 | jq --raw-output ".[0].\"HostConfig\".\"PortBindings\".\"$2/tcp\"[0].\"HostPort\"")
    echo $HOST_PORT
}

is_port_present() {
    # $1 - container name
    # $2 - container inner port
    # echo's 0 if present, otherwise > 0

    docker container inspect $1 | grep "\"$2/tcp\": \[" > /dev/null
    echo $?
}

test_values() {
    # $1 - actual
    # $2 - expected
    # $3 - error message
    if [ "$1" = "$2" ] 
    then echo -n ✅ 
    else echo -e "\n❌ $3" && exit 1 
    fi
}

test_docker_run() {
    local name="jsn-dkr-run"
    local status="exited"
    local image="nginx:mainline"
    local inner_port="80"
    local host_port="8888"

    local expected_present="1"
    local expected_host_port=$host_port
    local expected_inner_port="0"

    local result_present="$(is_container_present $name $status $image)"
    local result_host_port="$(get_host_port $name $inner_port)"
    local result_inner_port="$(is_port_present $name $inner_port)"

    local errormsg_present="контейнер не найден"
    local errormsg_host_port="неправильный порт хоста: $result_host_port"
    local errormsg_inner_port="неправильный порт внутри контейнера"

    echo -n "docker-run: "
    test_values "$result_present" "$expected_present" "$errormsg_present"
    test_values "$result_host_port" "$expected_host_port" "$errormsg_host_port"
    test_values "$result_inner_port" "$expected_inner_port" "$errormsg_inner_port"
    echo
}

test_docker_bind() {
    local name="jusan-docker-bind"
    local status="running"
    local image="nginx:mainline"
    local inner_port="80"
    local host_port="7777"

    local expected_present="1"
    local expected_host_port=$host_port
    local expected_inner_port="0"
    local expected_curl="Привет из Docker контейнера! 🐳"

    local result_present="$(is_container_present $name $status $image)"
    local result_host_port="$(get_host_port $name $inner_port)"
    local result_inner_port="$(is_port_present $name $inner_port)"
    local result_curl="$(curl -s http://localhost:$host_port | awk NF)"

    local errormsg_present="контейнер не найден"
    local errormsg_host_port="неправильный порт хоста: $result_host_port"
    local errormsg_inner_port="неправильный порт внутри контейнера"
    local errormsg_curl="неправильный ответ от контейнера: $result_curl"

    echo -n "docker-bind: "
    test_values "$result_present" "$expected_present" "$errormsg_present"
    test_values "$result_host_port" "$expected_host_port" "$errormsg_host_port"
    test_values "$result_inner_port" "$expected_inner_port" "$errormsg_inner_port"
    test_values "$result_curl" "$expected_curl" "$errormsg_curl"
    echo
}

test_docker_mount() {
    local name="jusan-docker-mount"
    local status="running"
    local image="nginx:mainline"
    local inner_port="80"
    local host_port="9999"

    local expected_present="1"
    local expected_host_port=$host_port
    local expected_inner_port="0"
    local expected_curl_root="<h1>Hello, from jusan-docker-mount</h1>"
    local expected_curl_test="Singularity"
    local expected_curl_token="Jusan"

    local result_present="$(is_container_present $name $status $image)"
    local result_host_port="$(get_host_port $name $inner_port)"
    local result_inner_port="$(is_port_present $name $inner_port)"
    local result_curl_root="$(curl -s -H "Host: example.com" http://localhost:$host_port | awk NF)"
    local result_curl_test="$(curl -s -H "Host: example.com" http://localhost:$host_port/test | awk NF)"
    local result_curl_token="$(curl -s -H "Host: example.com" http://localhost:$host_port/token | awk NF)"

    local errormsg_present="контейнер не найден"
    local errormsg_host_port="неправильный порт хоста: $result_host_port"
    local errormsg_inner_port="неправильный порт внутри контейнера"
    local errormsg_curl_root="неправильный ответ от контейнера: http://localhost:$host_port"
    local errormsg_curl_test="неправильный ответ от контейнера: http://localhost:$host_port/test"
    local errormsg_curl_token="неправильный ответ от контейнера: http://localhost:$host_port/token"

    echo -n "docker-mount: "
    test_values "$result_present" "$expected_present" "$errormsg_present"
    test_values "$result_host_port" "$expected_host_port" "$errormsg_host_port"
    test_values "$result_inner_port" "$expected_inner_port" "$errormsg_inner_port"
    test_values "$result_curl_root" "$expected_curl_root" "$errormsg_curl_root"
    test_values "$result_curl_test" "$expected_curl_test" "$errormsg_curl_test"
    test_values "$result_curl_token" "$expected_curl_token" "$errormsg_curl_token"
    echo
}

test_docker_exec() {
    local name="jusan-docker-exec"
    local status="running"
    local image="nginx:mainline"
    local inner_port="80"
    local host_port="8181"

    local expected_present="1"
    local expected_host_port=$host_port
    local expected_inner_port="0"
    local expected_curl_root="Hello, from jusan-docker-exec"
    local expected_curl_home="This is my home!"
    local expected_curl_about="I am just an exercise!"

    local result_present="$(is_container_present $name $status $image)"
    local result_host_port="$(get_host_port $name $inner_port)"
    local result_inner_port="$(is_port_present $name $inner_port)"
    local result_curl_root="$(curl -s -H "Host: jusan.singularity" http://localhost:$host_port | awk NF)"
    local result_curl_home="$(curl -s -H "Host: jusan.singularity" http://localhost:$host_port/home | awk NF)"
    local result_curl_about="$(curl -s -H "Host: jusan.singularity" http://localhost:$host_port/about | awk NF)"

    local errormsg_present="контейнер не найден"
    local errormsg_host_port="неправильный порт хоста: $result_host_port"
    local errormsg_inner_port="неправильный порт внутри контейнера"
    local errormsg_curl_root="неправильный ответ от контейнера: http://localhost:$host_port"
    local errormsg_curl_home="неправильный ответ от контейнера: http://localhost:$host_port/home"
    local errormsg_curl_about="неправильный ответ от контейнера: http://localhost:$host_port/about"

    echo -n "docker-exec: "
    test_values "$result_present" "$expected_present" "$errormsg_present"
    test_values "$result_host_port" "$expected_host_port" "$errormsg_host_port"
    test_values "$result_inner_port" "$expected_inner_port" "$errormsg_inner_port"
    test_values "$result_curl_root" "$expected_curl_root" "$errormsg_curl_root"
    test_values "$result_curl_home" "$expected_curl_home" "$errormsg_curl_home"
    test_values "$result_curl_about" "$expected_curl_about" "$errormsg_curl_about"
    echo
}

test_dockerfile() {
    local name="jusan-dockerfile"
    local status="running"
    local image="nginx:jusan-dockerfile"
    local inner_port="80"
    local host_port="6060"

    local expected_present="1"
    local expected_host_port=$host_port
    local expected_inner_port="0"
    local expected_curl_root="<h1>Hello, from jusan-dockerfile!</h1>"
    local expected_curl_dockerfile="FROM nginx:mainline"
    local expected_curl_secret="jusan-dockerfile"
    local expected_curl_jusan="singularity"

    local result_present="$(is_container_present $name $status $image)"
    local result_host_port="$(get_host_port $name $inner_port)"
    local result_inner_port="$(is_port_present $name $inner_port)"
    local result_curl_root="$(curl -s -H "Host: jusan.dockerfile" http://localhost:$host_port | awk NF)"
    local result_curl_dockerfile="$(curl -s -H "Host: jusan.dockerfile" http://localhost:$host_port/dockerfile | awk NF)"
    local result_curl_secret="$(curl -s -H "Host: jusan.dockerfile" http://localhost:$host_port/secret | awk NF)"
    local result_curl_jusan="$(curl -s -H "Host: jusan.dockerfile" http://localhost:$host_port/jusan | awk NF)"

    local errormsg_present="контейнер не найден"
    local errormsg_host_port="неправильный порт хоста: $result_host_port"
    local errormsg_inner_port="неправильный порт внутри контейнера"
    local errormsg_curl_root="неправильный ответ от контейнера: http://localhost:$host_port"
    local errormsg_curl_dockerfile="неправильный ответ от контейнера: http://localhost:$host_port/dockerfile"
    local errormsg_curl_secret="неправильный ответ от контейнера: http://localhost:$host_port/secret"
    local errormsg_curl_jusan="неправильный ответ от контейнера: http://localhost:$host_port/jusan"

    echo -n "dockerfile: "
    test_values "$result_present" "$expected_present" "$errormsg_present"
    test_values "$result_host_port" "$expected_host_port" "$errormsg_host_port"
    test_values "$result_inner_port" "$expected_inner_port" "$errormsg_inner_port"
    test_values "$result_curl_root" "$expected_curl_root" "$errormsg_curl_root"
    test_values "$result_curl_dockerfile" "$expected_curl_dockerfile" "$errormsg_curl_dockerfile"
    test_values "$result_curl_secret" "$expected_curl_secret" "$errormsg_curl_secret"
    test_values "$result_curl_jusan" "$expected_curl_jusan" "$errormsg_curl_jusan"
    echo
}

test_dockerize() {
    local name="jusan-dockerize"
    local status="running"
    local image="jusan-fastapi-final:dockerized"
    local inner_port="8080"
    local host_port="8080"

    local expected_present="1"
    local expected_host_port=$host_port
    local expected_inner_port="0"
    local expected_curl_sum10n="55"
    local expected_curl_fibo="34"
    local expected_curl_reverse="olleh"
    local expected_curl_calculator="2"

    local result_present="$(is_container_present $name $status $image)"
    local result_host_port="$(get_host_port $name $inner_port)"
    local result_inner_port="$(is_port_present $name $inner_port)"
    local result_curl_sum10n="$(curl -s http://localhost:8080/sum1n/10 | jq --raw-output '.result')"
    local result_curl_fibo="$(curl -s http://localhost:8080/fibo\?n=10 | jq --raw-output '.result')"
    local result_curl_reverse="$(curl -s -X POST -H "string: hello" http://localhost:8080/reverse | jq --raw-output '.result')"
    local result_curl_calculator="$(curl -s -H "Content-Type: application/json" -X POST -d '{"expr": "1,+,1"}' http://localhost:8080/calculator | jq --raw-output '.result')"

    local errormsg_present="контейнер не найден"
    local errormsg_host_port="неправильный порт хоста: $result_host_port"
    local errormsg_inner_port="неправильный порт внутри контейнера"
    local errormsg_curl_sum10n="неправильный ответ от контейнера: http://localhost:8080/sum1n/10"
    local errormsg_curl_fibo="неправильный ответ от контейнера: http://localhost:8080/fibo\?n=10"
    local errormsg_curl_reverse="неправильный ответ от контейнера: http://localhost:8080/reverse"
    local errormsg_curl_calculator="неправильный ответ от контейнера: http://localhost:8080/calculator"

    echo -n "dockerize: "
    test_values "$result_present" "$expected_present" "$errormsg_present"
    test_values "$result_host_port" "$expected_host_port" "$errormsg_host_port"
    test_values "$result_inner_port" "$expected_inner_port" "$errormsg_inner_port"
    test_values "$result_curl_sum10n" "$expected_curl_sum10n" "$errormsg_curl_sum10n"
    test_values "$result_curl_fibo" "$expected_curl_fibo" "$errormsg_curl_fibo"
    test_values "$result_curl_reverse" "$expected_curl_reverse" "$errormsg_curl_reverse"
    test_values "$result_curl_calculator" "$expected_curl_calculator" "$errormsg_curl_calculator"
    echo
}

test_docker_compose() {
    local name="jusan-compose"
    local status="running"
    local image="jusan-fastapi-final:dockerized"
    local inner_port="8080"
    local host_port="8282"

    local expected_present="1"
    local expected_host_port=$host_port
    local expected_inner_port="0"
    local expected_curl_sum10n="55"
    local expected_curl_fibo="34"
    local expected_curl_reverse="olleh"
    local expected_curl_calculator="2"

    local result_present="$(is_container_present $name $status $image)"
    local result_host_port="$(get_host_port $name $inner_port)"
    local result_inner_port="$(is_port_present $name $inner_port)"
    local result_curl_sum10n="$(curl -s http://localhost:8080/sum1n/10 | jq --raw-output '.result')"
    local result_curl_fibo="$(curl -s http://localhost:8080/fibo\?n=10 | jq --raw-output '.result')"
    local result_curl_reverse="$(curl -s -X POST -H "string: hello" http://localhost:8080/reverse | jq --raw-output '.result')"
    local result_curl_calculator="$(curl -s -H "Content-Type: application/json" -X POST -d '{"expr": "1,+,1"}' http://localhost:8080/calculator | jq --raw-output '.result')"

    local errormsg_present="контейнер не найден"
    local errormsg_host_port="неправильный порт хоста: $result_host_port"
    local errormsg_inner_port="неправильный порт внутри контейнера"
    local errormsg_curl_sum10n="неправильный ответ от контейнера: http://localhost:8080/sum1n/10"
    local errormsg_curl_fibo="неправильный ответ от контейнера: http://localhost:8080/fibo\?n=10"
    local errormsg_curl_reverse="неправильный ответ от контейнера: http://localhost:8080/reverse"
    local errormsg_curl_calculator="неправильный ответ от контейнера: http://localhost:8080/calculator"

    echo -n "docker-compose: "
    test_values "$result_present" "$expected_present" "$errormsg_present"
    test_values "$result_host_port" "$expected_host_port" "$errormsg_host_port"
    test_values "$result_inner_port" "$expected_inner_port" "$errormsg_inner_port"
    test_values "$result_curl_sum10n" "$expected_curl_sum10n" "$errormsg_curl_sum10n"
    test_values "$result_curl_fibo" "$expected_curl_fibo" "$errormsg_curl_fibo"
    test_values "$result_curl_reverse" "$expected_curl_reverse" "$errormsg_curl_reverse"
    test_values "$result_curl_calculator" "$expected_curl_calculator" "$errormsg_curl_calculator"
    echo
}

test_docker_compose_final() {
    local name="jusan-nginx-final"
    local status="running"
    local image="nginx:mainline"
    local inner_port="80"
    local host_port="8787"

    local expected_present="1"
    local expected_host_port=$host_port
    local expected_inner_port="0"
    local expected_curl_sum10n="55"
    local expected_curl_fibo="34"
    local expected_curl_reverse="olleh"
    local expected_curl_calculator="2"

    local result_present="$(is_container_present $name $status $image)"
    local result_host_port="$(get_host_port $name $inner_port)"
    local result_inner_port="$(is_port_present $name $inner_port)"
    local result_curl_sum10n="$(curl -H "Host: jusan.docker-compose" -s http://localhost:$host_port/sum1n/10 | jq --raw-output '.result')"
    local result_curl_fibo="$(curl -H "Host: jusan.docker-compose" -s http://localhost:$host_port/fibo\?n=10 | jq --raw-output '.result')"
    local result_curl_reverse="$(curl -H "Host: jusan.docker-compose" -s -X POST -H "string: hello" http://localhost:$host_port/reverse | jq --raw-output '.result')"
    local result_curl_calculator="$(curl -H "Host: jusan.docker-compose" -s -H "Content-Type: application/json" -X POST -d '{"expr": "1,+,1"}' http://localhost:$host_port/calculator | jq --raw-output '.result')"

    local errormsg_present="контейнер не найден"
    local errormsg_host_port="неправильный порт хоста: $result_host_port"
    local errormsg_inner_port="неправильный порт внутри контейнера"
    local errormsg_curl_sum10n="неправильный ответ от контейнера: http://localhost:$host_port/sum1n/10"
    local errormsg_curl_fibo="неправильный ответ от контейнера: http://localhost:$host_port/fibo\?n=10"
    local errormsg_curl_reverse="неправильный ответ от контейнера: http://localhost:$host_port/reverse"
    local errormsg_curl_calculator="неправильный ответ от контейнера: http://localhost:$host_port/calculator"

    echo -n "docker-compose-final: "
    test_values "$result_present" "$expected_present" "$errormsg_present"
    test_values "$result_host_port" "$expected_host_port" "$errormsg_host_port"
    test_values "$result_inner_port" "$expected_inner_port" "$errormsg_inner_port"
    test_values "$result_curl_sum10n" "$expected_curl_sum10n" "$errormsg_curl_sum10n"
    test_values "$result_curl_fibo" "$expected_curl_fibo" "$errormsg_curl_fibo"
    test_values "$result_curl_reverse" "$expected_curl_reverse" "$errormsg_curl_reverse"
    test_values "$result_curl_calculator" "$expected_curl_calculator" "$errormsg_curl_calculator"
    echo
}

test_docker_run
test_docker_bind
test_docker_mount
test_docker_exec
test_dockerfile
test_dockerize
test_docker_compose
test_docker_compose_final
