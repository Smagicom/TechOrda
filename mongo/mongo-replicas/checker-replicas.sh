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


RS_STATUS="$(docker exec mongo-replicas_mongo-1_1 mongo --quiet --eval "JSON.stringify(rs.status())")"

RS_LENGTH=$(echo $RS_STATUS | jq '.members | length')
PRIMARY_NAME=$(echo $RS_STATUS | jq -r '.members[] | select(.state==1) | .name' | cut -d ':' -f1)
PRIMARY_PORT=$(echo $RS_STATUS | jq -r '.members[] | select(.state==1) | .name' | cut -d ':' -f2)


COLLECTIONS=$(docker exec -i $PRIMARY_NAME mongo --quiet --port $PRIMARY_PORT << EOF | tail -n1
use reservations
db.getCollectionNames()
EOF
)

test_values "$RS_LENGTH" "3" "Должно быть 3 сервера в реплика сете"
test_values "$COLLECTIONS" '[ "rooms", "user_reservations", "users" ]' "Бэкап reservations не поднят"
