# nginx-install

В данном уроке разберем как правильно устанавливать `nginx` на сервер.

### Стандартный репозиторий

Пакет `nginx` доступен в репозитории пакетов `apt` в Ubuntu. Однако, в
зависимости от версии Ubuntu - версия пакета `nginx` может быть устарелой.
Если установить на Ubuntu 18.04, то скачается версия от 17 Апреля 2018 г. - `1.14.0`.

```bash
$ apt install nginx
$ nginx -v
nginx version: nginx/1.14.0 (Ubuntu)
```

### Официальный репозиторий

Поэтому, чтобы иметь актуальную версию `nginx`, нужно скачивать пакет из
официального репозитория.

Создать файл `/etc/apt/sources.list.d/nginx.list`, который содержит:

```
deb http://nginx.org/packages/mainline/OS/ CODENAME nginx
deb-src http://nginx.org/packages/mainline/OS/ CODENAME nginx
```

Измените файл, заменив `OS` в конце URL-адреса на `ubuntu` или `debian`, в зависимости
от вашей операционной системы.

Замените `CODENAME` на кодовое имя вашего дистрибутива;

- `jessie` или `stretch` для Debian,
- `trusty`, `xenial`, `artful`, или `bionic` для Ubuntu.

Чтобы узнать `CODENAME`.

```bash
cat /etc/os-release
```

Затем, запустите следующие команды:

```bash
apt update
apt install -y gnupg2
curl -sLO http://nginx.org/keys/nginx_signing.key
apt-key add nginx_signing.key
apt update
apt install -y nginx
```

Проверим версию `nginx`.

```bash
$ nginx -v
nginx version: nginx/1.21.6
```

Версия `1.21.6` выпущена 25 января 2022 года. Она является на момент написания
урока актуальной.

> ⭐️ Задания в данном модуле необходимо выполнять с помощью актуальной версии nginx.

### Полезное

- [инструкция c официального сайта nginx](https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-open-source/#installing-a-prebuilt-debian-package-from-the-official-nginx-repository)

### Задание

1. Установить на удаленном сервере stepik наиболее актуальную версию `nginx`.

Для проверки выполните запрос на `127.0.0.1`

```bash
curl http://127.0.0.1
```

Должен прийти такой ответ.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Welcome to nginx!</title>
    <style>
      body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
      }
    </style>
  </head>
  <body>
    <h1>Welcome to nginx!</h1>
    <p>
      If you see this page, the nginx web server is successfully installed and
      working. Further configuration is required.
    </p>

    <p>
      For online documentation and support please refer to
      <a href="http://nginx.org/">nginx.org</a>.<br />
      Commercial support is available at
      <a href="http://nginx.com/">nginx.com</a>.
    </p>

    <p><em>Thank you for using nginx.</em></p>
  </body>
</html>
```

---

### Ответ
