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


NODE1="$(docker ps -q -f "name=rabbit-1")"
NODE2="$(docker ps -q -f "name=rabbit-2")"

docker exec -it rabbit-1 rabbitmqctl cluster_status | grep "rabbit@$NODE1" > /dev/null
STATUS1="$?"

docker exec -it rabbit-1 rabbitmqctl cluster_status | grep "rabbit@$NODE2" > /dev/null
STATUS2="$?"

echo -n "cluster: "
test_values $STATUS1 $STATUS2 "rabbit-1 и rabbit-2 не объединены в кластер"
echo
