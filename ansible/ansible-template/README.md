# ansible-template

Для текущего задания мы подготовили `docker-compose.yaml`:

```yaml
services:
  local-vps-22:
    image: atlekbai/local-vps:latest
    container_name: local-vps-22
    ports:
      - "22:22"
      - "80:80"
      - "7070:7070"
      - "8080:8080"
      - "8888:8888"
      - "9090:9090"
    restart: always
    command: "22"
```

Используйте его для запуска учебного контейнера.

> ❗️ Не забудьте залить на сервер ssh-ключ с помощью `ssh-copy-id`.

### Полезное

- [Документация Jinja2][jinja_doc]
- [Модуль copy в Ansible][copy_module]
- [Модуль file в Ansible][file_module]
- [Модуль template в Ansible][template_module]

[jinja_doc]: https://jinja.palletsprojects.com/en/3.1.x/templates/#synopsis
[apt_module]: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_module.html
[service_module]: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/service_module.html
[copy_module]: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/copy_module.html
[file_module]: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/file_module.html
[template_module]: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/template_module.html

### Задание

1. В репозитории `jusan-ansible` создайте ветку `template`. Вести работу будем в ней.
2. Создать шаблон `server.conf.j2` для nginx сервер блока, который принимает переменные
   и преобразует в файл.

```yaml
server_port: 80
server_name: example.com
locations:
  - path: /
    status_code: 200
    message: Welcome to main page!
  - path: /about
    status_code: 202
    message: This is our about page.
  - path: /user
    status_code: 201
    message: User page
```

```nginx
server {
    listen 80;
    server_name example.com;

    location / {
        return 200 'Welcome to main page!';
    }

    location /about {
        return 202 'This is our about page';
    }

    location /user {
        return 201 'User page';
    }
}
```

3. Отредактировать `playbook.yaml`:
   - Запускается только для хостов группы `lb`;
   - В разделе `handlers` есть один таск `reload-nginx`, который перезагружает nginx;
   - Для каждого таска в разделе `tasks` подбирайте подходящее название `name`,
     которое четко описывает операцию;
   - Устанавливает nginx;
   - Копирует [nginx.conf](./nginx.conf) на место основного конфигурационного файла nginx,
     вызывает хендлер `reload-nginx`;
   - Удаляет `default.conf`. Найдите откуда нужно удалить.
   - Использует шаблонизатор `template` чтобы сгенерировать файлы на сервере. Записывайте
     каждый файл по пути `/etc/nginx/conf.d/{{ item.server_name }}.conf`, использовать `loop`.
     После выполнения вызовите хендлер `reload-nginx`. В `loop` использовать следующие элементы:

```yaml
- server_port: 7070
  server_name: jmart-ansible.kz
  locations:
    - path: /main
      status_code: 200
      message: Добро пожаловать на JMart!
    - path: /profile
      status_code: 201
      message: Это страница профиля.

- server_port: 8080
  server_name: jusan-ansible.kz
  locations:
    - path: /
      status_code: 200
      message: Добро пожаловать на Jusan Bank!
    - path: /account
      status_code: 202
      message: Здесь ваш банковский счет!

- server_port: 9090
  server_name: invest-ansible.kz
  locations:
    - path: /home
      status_code: 200
      message: Добро пожаловать на Jusan Invest!
    - path: /user
      status_code: 203
      message: Это страница с вашим брокерским счетом.
```

4. Запушить в гит. В папке должен присутствовать `docker-compose.yaml`

Чтобы проверить правильно ли запущено все, запустите тестировщик [checker-template.sh](https://stepik.org/media/attachments/lesson/698792/checker-template.sh).

```bash
bash checker-template.sh
```

---

### Ответ
