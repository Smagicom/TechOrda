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
