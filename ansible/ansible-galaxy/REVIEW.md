## Рецензия

### Дополнительная информация

<img src="../../../resources/code-review.png" alt="code-review.png" width="250"/>

Рецензия - это проверка проекта другого учащегося. Перед тем, как приступить к рецензированию, ознакомьтесь с правилами проведения рецензии.

**Правила рецензии:**

- Проверять только выполненную работу.
- Следовать указаниям критериев оценки.
- Если проект учащегося соответствует критерию, то ставьте 1.
- Если проект учащегося не соответствует критерию, то ставьте 0.

### Критерий оценки #1

GitHub ссылка рабочая и ведет на репозиторий с выполненным заданием.

Если это не так, то ставьте оценку 0 и заканчивайте проверку.

### Критерий оценки #2

Проверим задание `ansible-playbook`.

1. В репо есть файлы: `setup.sh`, `hosts.ini`, `playbook.yml`.

2. Запустите следующие команды:

```bash
bash ./setup.sh
ansible-playbook -i hosts.ini playbook.yaml
```

Зайдите [localhost](http://localhost/) - должна выйти приветственная страница nginx.

3. Проверьте `hosts.ini` - в ней должна быть только одна группа `lb`.
4. Проверьте `playbook.yaml` - в `hosts` должно быть значение `lb`.

### Критерий оценки #3

Проверим задание `ansible-template`. Для этого перейдите на ветку `template`.

```bash
git checkout template
```

1. В репо есть новые файлы: `server.conf.j2`, `nginx.conf`, `docker-compose.yaml`.
2. Запустите следующие команды:

```bash
docker-compose up -d
ssh-copy-id -p 22 root@127.0.0.1
ansible-playbook -i hosts.ini playbook.yaml
```

3. Запустите [тестировщик](https://stepik.org/media/attachments/lesson/698792/checker-template.sh):

```bash
bash checker-template.sh
```

4. В `playbook.yaml` есть таск, которые использует модуль `template` и след. переменны:

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

5. В `server.conf.j2` определен примерно такой шаблон:

```nginx
server {
    listen {{ server_port }};

    server_name {{ server_name }};

    {% for item in locations %}
    location {{ item.path }} {
        return {{ item.status_code }} '{{ item.message }}';
    }
    {% endfor %}
}
```

### Критерий оценки #4

Проверим задание `ansible-apps`. Для этого перейдите на ветку `apps`.

1. В репо есть директории: `files`, `templates`.
2. В корневой директории присутствуют только `docker-compose.yaml`, `hosts.ini`, `playbook.yaml`.
3. В `files` есть файлы: `nginx.conf`, `api.service`.
4. В `templates` есть файлы: `app.conf.j2`, `server.conf.j2`.
5. Запустите следующие команды:

```bash
docker-compose up -d
ansible-playbook -i hosts.ini playbook.yaml
```

6. Запустите [тестировщик](https://stepik.org/media/attachments/lesson/698792/checker-apps.sh):

```bash
bash checker-apps.sh
```

7. В `playbook.yaml` в тасках для хостов `lb` появился таск `template`, который использует
   переменные и вызывает хендлер `reload-nginx`:

```yaml
server_port: 80
server_name: jusan-apps.kz
apps:
  - local-vps-23:9090
  - local-vps-24:9090
```

8. В `playbook.yaml` есть таски для группы хостов `app`.
9. В `hosts.ini` есть группа `app` с двумя хостами.
10. В `templates/app.conf.j2` есть шаблон который похож на следующий:

```nginx
upstream app {
{% for item in apps %}
    server {{ item }};
{% endfor %}
}

server {
    listen {{ server_port }};
    server_name {{ server_name }};
    location / {
        proxy_pass http://app;
        add_header  X-Upstream  $upstream_addr;
    }
}
```

### Критерий оценки #5

Проверим задание `ansible-roles`. Для этого перейдите на ветку `roles`.

1. В корневой директории присутствуют только `docker-compose.yaml`, `hosts.ini`, `playbook.yaml` и
   директория `roles`.
2. В директории `roles` есть 3 папки `nginx`, `nginx-configuration`, `application`.
3. Запустите следующие команды:

```bash
docker-compose up -d
ansible-playbook -i hosts.ini playbook.yaml
```

4. Запустите [тестировщик](https://stepik.org/media/attachments/lesson/698792/checker-apps.sh):

```bash
bash checker-apps.sh
```

5. В `playbook.yaml` используются только роли, нет ни одного таска.
6. В каждой папке роли проверьте `meta/main.yaml`, в ней должна содержаться `short_description`
   роли, которые описывает что делает роль. Должно по смыслу подходить след.:
   - `nginx` - установка nginx;
   - `nginx-configuration` - настройка конфигурации nginx;
   - `application` - установка app

### Критерий оценки #6

Проверим задание `ansible-vault`. Для этого перейдите на ветку `vault`.

1. В корневой директории должен появиться новый файл `vars/nginx_secret_token.yaml`.
2. Запустите следующие команды:

```bash
docker-compose up -d
ansible-playbook -i hosts.ini playbook.yaml --ask-vault-pass
```

Запросит пароль - `kazakhstan2022`.

4. Запустите [тестировщик](https://stepik.org/media/attachments/lesson/698792/checker-vault.sh):

```bash
bash checker-vault.sh
```

5. Есть новый файл `roles/nginx-configuration/templates/` который создает `location /secret`.
6. В `playbook.yaml` под тасками хостов `lb` подключается файл переменных `vars/nginx_secret_token.yaml`.
7. Во всем репо не встречается секретный текст `Jusan Singularity`, чтобы найти такое введите:

```bash
grep -rnw . -e 'Jusan Singularity'
```

### Критерий оценки #7

Проверим задание `ansible-galaxy`. Для этого перейдите на ветку `galaxy`.

1. В репозиторий появился файл `requirements.yaml`, который содержит роль `geerlingguy.nginx`
   как зависимость.
2. Запустите следующие команды:

```bash
ansible-galaxy install -r requirements.yaml
docker-compose up -d
ansible-playbook -i hosts.ini playbook.yaml --ask-vault-pass
```

Запросит пароль - `kazakhstan2022`.

4. Запустите [тестировщик](https://stepik.org/media/attachments/lesson/698792/checker-vault.sh):

```bash
bash checker-vault.sh
```

5. В `playbook.yaml` использует роль `geerlingguy.nginx` для хостов `lb`.
6. В директории `roles` удалена роль `nginx`.
