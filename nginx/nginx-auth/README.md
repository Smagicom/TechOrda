# nginx-auth

### Задание

1. Настройте `server` блок, который слушает 8080 порт.
2. Установите `server_name` значению `example.com`.
3. Добавьте `location` блок для пути `/`, который обслуживает файл [index.html](https://stepik.org/media/attachments/lesson/686238/index.html)
4. Добавьте `location` блок для пути `/images`, который обслуживает файлы из архива [cats.zip](https://stepik.org/media/attachments/lesson/686238/cats.zip). Установите авторизованный вход для учетки: `design:SteveJobs1955`, т.е. логин `design`, пароль `SteveJobs1955`.
5. Добавьте `location` блок для пути `/gifs`, который обслуживает файлы из архива [gifs.zip](https://stepik.org/media/attachments/lesson/686238/gifs.zip). Установите авторизованный вход для учетки: `marketing:marketingP@ssword`.
6. Учетка `design` не должна иметь доступ на другие пути, тоже самое касается других учеток.

---

  GNU nano 7.2                                                                hwnginx.conf                                                                         
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
        return 201 'jusan-nginx-locations';
    }

    location /api/ {
        proxy_pass http://localhost:9090;
    }
}


