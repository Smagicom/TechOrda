# nginx-ip

Защита ценных ресурсов и сервисов в Интернете должна осуществляться поэтапно. NGINX является одним из этих этапов.

Директива `deny` блокирует доступ к конкретному блоку, а директива `allow` может использоваться для
разрешения подмножества заблокированного доступа. Вы можете использовать IP-адреса, IPv4 или IPv6, и ключевое слово `all`.

Как правило, при защите ресурса можно запретить доступ для всех к определенному `location` блоку и разрешить доступ только с определенных IP адресов.

### Полезные ссылки

- [Restricting Access by IP Address ](https://docs.nginx.com/nginx/admin-guide/security-controls/controlling-access-proxied-tcp/)
- [How to block/allow IP-addresses in Nginx](https://support.hypernode.com/en/hypernode/nginx/how-to-block-allow-ip-addresses-in-nginx)

### Задание

1. Настройте `server` блок, который слушает 8080 порт.
2. Установите `server_name` равным значению `example.com`.
3. Добавьте `location /secret_word`, который возвращает строку `jusan-nginx-ip` со статусом `203`. Разрешите доступ к блоку из `192.0.0.1/20` кроме `192.0.0.1` и запретите все остальные.
4. Отправьте получившийся результат.

---

### Ответ

  GNU nano 7.2                                                                hwnginx.conf *                                                                       
server {
    listen 8080;
    server_name example.com;
    location / {
        auth_basic "private site";
        auth_basic_user_file /etc/nginx/conf.d/passwd;
        root /var/www/example.com;
        index index.html;
    }
    location /images {
        auth_basic "design site";
        auth_basic_user_file /etc/nginx/conf.d/design_passwd;
        root /var/www/example.com/cats/;
    }
    location /gifs {
        auth_basic "marketing site";
        auth_basic_user_file /etc/nginx/conf.d/marketing_passwd;
        root /var/www/example.com/gifs/;
    }

    location /secret_word {
        allow 192.0.0.1/20;       
        deny 192.0.0.1;           
        deny all;                
        return 203 'jusan-nginx-ip'; 
    }

    location /api/ {
        proxy_pass http://localhost:9090;
    }
}

curl http://localhost:8080/secret_word
jusan-nginx-ip

