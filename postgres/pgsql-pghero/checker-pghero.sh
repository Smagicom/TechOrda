#!/usr/bin/env bash

test_values() {
    # $1 - actual
    # $2 - expected
    # $3 - error message
    if [ "$1" = "$2" ] 
    then echo -n ✅ 
    else echo -e "\n❌ $3" && exit 1 
    fi
}

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

test_query_stats() {
    local stats="shared_preload_libraries=pg_stat_statements
    pg_stat_statements.track=all
    pg_stat_statements.max=10000
    track_activity_query_size=2kB"
    echo -n "query stats: "
    for stat in $stats ; do
        local key=$(echo $stat | cut -d '=' -f1)
        local val=$(echo $stat | cut -d '=' -f2)
        local cmd="show $key"
        local act=$(docker exec -it jusan-postgres psql -qtAX -U postgres -c "$cmd" | tr -d '\r')
        test_values "$act" "$val" "query stat conf not enabled: $key"
    done
    echo
}

test_deadline() {
    local exp="10 MB"

    local cmd="\l+"
    local act=$(docker exec -it jusan-postgres psql -qtAX -U postgres -c "$cmd" | tr -d '\r' | grep deadline | cut -d '|' -f 7)

    local err="deadline database not present"

    echo -n "deadline database: "
    test_values "$act" "$exp" "$err"
    echo
}

test_postgres() {
    local name="jusan-postgres"
    local status="running"
    local image="postgres:14"
    local inner_port="5432"
    local host_port="5432"

    local act_present="$(is_container_present $name $status $image)"
    local exp_present="1"
    local err_present="$name container not running"

    local act_host_port="$(get_host_port $name $inner_port)"
    local exp_host_port=$host_port
    local err_host_port="$name is not running on desired host port"

    local act_inner_port="$(is_port_present $name $inner_port)"
    local exp_inner_port="0"
    local err_inner_port="$name is not running on desired inner port"

    echo -n "$name: "
    test_values "$act_present" "$exp_present" "$err_present"
    test_values "$act_host_port" "$exp_host_port" "$err_host_port"
    test_values "$act_inner_port" "$exp_inner_port" "$err_inner_port"
    echo
}

test_pghero() {
    local name="jusan-pghero"
    local status="running"
    local image="ankane/pghero:v2.8.2"
    local inner_port="8080"
    local host_port="8080"

    local act_present="$(is_container_present $name $status $image)"
    local exp_present="1"
    local err_present="$name container not running"

    local act_host_port="$(get_host_port $name $inner_port)"
    local exp_host_port=$host_port
    local err_host_port="$name is not running on desired host port"

    local act_inner_port="$(is_port_present $name $inner_port)"
    local exp_inner_port="0"
    local err_inner_port="$name is not running on desired inner port"

    echo -n "$name: "
    test_values "$act_present" "$exp_present" "$err_present"
    test_values "$act_host_port" "$exp_host_port" "$err_host_port"
    test_values "$act_inner_port" "$exp_inner_port" "$err_inner_port"
    echo
}

test_query_stats
test_deadline
test_postgres
test_pghero
