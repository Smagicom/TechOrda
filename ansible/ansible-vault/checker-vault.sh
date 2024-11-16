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

umsg() {
    # $1 - host 
    # $2 - path
    curl -s -H "Host: $1" "$2"
}

ucode() {
    # $1 - host 
    # $2 - path
    curl -sI -H "Host: $1" $2 | head -n1 | cut -d ' ' -f2
}

ustream() {
    # $1 - host 
    # $2 - path
    curl -sI -H "Host: $1" $2 | grep X-Upstream
}

test_nginx() {
    # actual
    local act7070_main_msg=$(umsg "jmart-ansible.kz" "http://localhost:7070/main")
    local act7070_main_code=$(ucode "jmart-ansible.kz" "http://localhost:7070/main")
    local act7070_profile_msg=$(umsg "jmart-ansible.kz" "http://localhost:7070/profile")
    local act7070_profile_code=$(ucode "jmart-ansible.kz" "http://localhost:7070/profile")
    
    local act8080_main_msg=$(umsg "jusan-ansible.kz" "http://localhost:8080/")
    local act8080_main_code=$(ucode "jusan-ansible.kz" "http://localhost:8080/")
    local act8080_account_msg=$(umsg "jusan-ansible.kz" "http://localhost:8080/account")
    local act8080_account_code=$(ucode "jusan-ansible.kz" "http://localhost:8080/account")

    local act9090_home_msg=$(umsg "invest-ansible.kz" "http://localhost:9090/home")
    local act9090_home_code=$(ucode "invest-ansible.kz" "http://localhost:9090/home")
    local act9090_user_msg=$(umsg "invest-ansible.kz" "http://localhost:9090/user")
    local act9090_user_code=$(ucode "invest-ansible.kz" "http://localhost:9090/user")

    local act8888_msg=$(umsg "123" "http://localhost:8888/")
    local act8888_code=$(ucode "123" "http://localhost:8888/")
    
    # expected 
    local exp7070_main_msg="Добро пожаловать на JMart!"
    local exp7070_main_code="200"
    local exp7070_profile_msg="Это страница профиля."
    local exp7070_profile_code="201"

    local exp8080_main_msg="Добро пожаловать на Jusan Bank!"
    local exp8080_main_code="200"
    local exp8080_account_msg="Здесь ваш банковский счет!"
    local exp8080_account_code="202"

    local exp9090_home_msg="Добро пожаловать на Jusan Invest!"
    local exp9090_home_code="200"
    local exp9090_user_msg="Это страница с вашим брокерским счетом."
    local exp9090_user_code="203"

    local exp8888_msg="hello, from nginx.conf"
    local exp8888_code="222"

    # error messages
    local err7070_main_msg="Wrong response: Host: jmart-ansible.kz URL: http://localhost:7070/main"
    local err7070_main_code="Wrong status code: Host: jmart-ansible.kz URL: http://localhost:7070/main"
    local err7070_profile_msg="Wrong response: Host: jmart-ansible.kz URL: http://localhost:7070/profile"
    local err7070_profile_code="Wrong status code: Host: jmart-ansible.kz URL: http://localhost:7070/profile"

    local err8080_main_msg="Wrong response: Host: jusan-ansible.kz URL: http://localhost:8080/"
    local err8080_main_code="Wrong status code: Host: jusan-ansible.kz URL: http://localhost:8080/"
    local err8080_account_msg="Wrong response: Host: jusan-ansible.kz URL: http://localhost:8080/account"
    local err8080_account_code="Wrong status code: Host: jusan-ansible.kz URL: http://localhost:8080/account"

    local err9090_home_msg="Wrong response: Host: invest-ansible.kz URL: http://localhost:9090/home"
    local err9090_home_code="Wrong status code: Host: invest-ansible.kz URL: http://localhost:9090/home"
    local err9090_user_msg="Wrong response: Host: invest-ansible.kz URL: http://localhost:9090/user"
    local err9090_user_code="Wrong status code: Host: invest-ansible.kz URL: http://localhost:9090/user"

    local err8888_msg="Wrong response: http://localhost:8888/"
    local err8888_code="Wrong status code: http://localhost:8888/"

    echo -n "nginx: "
    test_values "$act7070_main_msg" "$exp7070_main_msg" "$err7070_main_msg"
    test_values "$act7070_main_code" "$exp7070_main_code" "$err7070_main_code"
    test_values "$act7070_profile_msg" "$exp7070_profile_msg" "$err7070_profile_msg"
    test_values "$act7070_profile_code" "$exp7070_profile_code" "$err7070_profile_code"
    
    test_values "$act8080_main_msg" "$exp8080_main_msg" "$err8080_main_msg"
    test_values "$act8080_main_code" "$exp8080_main_code" "$err8080_main_code"
    test_values "$act8080_account_msg" "$exp8080_account_msg" "$err8080_account_msg"
    test_values "$act8080_account_code" "$exp8080_account_code" "$err8080_account_code"

    test_values "$act9090_home_msg" "$exp9090_home_msg" "$err9090_home_msg"
    test_values "$act9090_home_code" "$exp9090_home_code" "$err9090_home_code"
    test_values "$act9090_user_msg" "$exp9090_user_msg" "$err9090_user_msg"
    test_values "$act9090_user_code" "$exp9090_user_code" "$err9090_user_code"

    test_values "$act8888_msg" "$exp8888_msg" "$err8888_msg"
    test_values "$act8888_code" "$exp8888_code" "$err8888_code"
    echo
}

test_app() {
    local act_msg="$(umsg "jusan-apps.kz" "http://localhost/" | cut -d ':' -f1 )"
    local act_head="$(ustream "jusan-apps.kz" "http://localhost/" | cut -d ':' -f3 | xargs echo -n)"
    act_head="${act_head:0:4}"

    local exp_msg="web-server"
    local exp_head="9090"

    local err_msg="wrong response from app"
    local err_head="upstream header not present"

    echo -n "app: "
    test_values "$act_msg" "$exp_msg" "$err_msg"
    test_values "$act_head" "$exp_head" "$err_head"
    echo
}

test_secret() {
    local act_msg="$(umsg "jusan-secret.kz" "http://localhost:9090/secret")"
    local exp_msg="Jusan Singularity"
    local err_msg="wrong response from secret"

    echo -n "secret: "
    test_values "$act_msg" "$exp_msg" "$err_msg"
    test_values "$act_head" "$exp_head" "$err_head"
    echo
}

test_nginx
test_app
test_secret
