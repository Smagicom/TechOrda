# nginx-locations

### Полезное

- [Downloading files with curl ](http://www.compciv.org/recipes/cli/downloading-with-curl/)
- [unzip](https://askubuntu.com/questions/86849/how-to-unzip-a-zip-file-from-the-terminal)
- [nginx: alias](http://nginx.org/en/docs/http/ngx_http_core_module.html#alias)
- [nginx location 404 not found](https://stackoverflow.com/questions/41099318/nginx-location-404-not-found)

### Задание

1. Настройте `server` блок, который слушает 8080 порт.
2. Установите `server_name` равным значению `example.com`.
3. Добавьте `location` блок для пути `/`, который обслуживает файл [index.html](https://stepik.org/media/attachments/lesson/686238/index.html). Файл должен быть неизмененным - если будете копировать-вставлять текст из файле, то возможно может добавиться лишний символ.
4. Добавьте `location` блок для пути `/images`, который обслуживает файлы из архива [cats.zip](https://stepik.org/media/attachments/lesson/686238/cats.zip)
5. Добавьте `location` блок для пути `/gifs`, который обслуживает файлы из архива [gifs.zip](https://stepik.org/media/attachments/lesson/686238/gifs.zip)
6. Добавьте `location` блок для пути `/secret_word`, который возвращает строку `jusan-nginx-locations` со статусом `201`.

Чтобы проверить запрос на созданный `server` блок, запустите команду.

```bash
curl -H "Host: example.com" http://localhost:8080/
```

---

### Ответ
server {
    listen 8080;
    server_name example.com;
    location / {
        root /var/www/example.com;
        index index.html;
    }
    location /images {
        alias /var/www/example.com/cats/;
    }
    location /gifs {
        alias /var/www/example.com/gifs/;
    }
    location /secret_word {
        return 201 'jusan-nginx-locations';
    }
}


curl -H "Host: example.com" http://localhost:8080/

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cats Page</title>
</head>

<body>
    <p>
    <h1>Cat with Flower</h1>
    <img src="/images/flower.png" alt="flower">
    </p>

    <p>
    <h1>Cat with Glasses</h1>
    <img src="/images/glasses.png" alt="glasses">
    </p>

    <p>
    <h1>Gray Cat</h1>
    <img src="/images/gray-animal.jpeg" alt="gray-animal">
    </p>

    <p>
    <h1>Cats mafia</h1>
    <img src="/images/mafia.png" alt="mafia">
    </p>

    <p>
    <h1>Sleepy Cat</h1>
    <img src="/images/sleep.png" alt="sleep">
    </p>
</body>

</html>
