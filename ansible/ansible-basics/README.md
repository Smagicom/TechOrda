# ansible-basics

Первые шаги по запуску простейшых команд через Ansible, уже разобраны: мы
научились устанавливать nginx и запускать его как сервис. Для этого были
использованы модули [apt][apt_module] и [service][service_module].

## Handlers

А теперь представим, что нужно залить файл конфигурации nginx из нашего компьютера
на сервер и если команда выполнилась успешно, то нужно перезагрузить сервис nginx.

Сначала напишем команду копирования файла на сервер через модуль [copy][copy_module].

```yaml
---
- hosts: all
  become: yes

  tasks:
    - apt: name=nginx state=present
    - copy: # <----------- вызываем модуль copy
        src: ./jusan.conf
        dest: /etc/nginx/conf.d/jusan.conf
```

После этого мы добавим еще один новый раздел в плейбук - `handlers`:

```yaml
---
- hosts: all
  become: yes

  tasks:
    - apt: name=nginx state=present
    - copy:
        src: ./jusan.conf
        dest: /etc/nginx/conf.d/jusan.conf

  handlers: # <----------- добавляем новый раздел handlers
    - name: reload nginx
      service: name=nginx state=reloaded
```

`handler` (рус. "обработчик") — это вид тасков, которые запускаются после успешного выполнения команды.
Обработчик будет вызываться только в том случае, если задача вносит изменения на сервер и была выполнена
без ошибок. Чтобы вызывать его, нужно указать опцию `notify` в таске с указанием названия обработчика.

```yaml
- copy:
    src: ./jusan.conf
    dest: /etc/nginx/conf.d/jusan.conf
  notify: reload nginx # <------ вызываем handler с таким названием
```

## Циклы

В плейбуках можно определять циклы. Например нам нужно создать несколько пользователей
в системе, и вместо того чтобы создавать отдельный таск под каждого пользователя, можно
создать их через цикл `loop`.

```yaml
- name: Добавление пользователей
  user:
    name: "{{ item }}"
    state: present
    groups: "admin"
  loop:
    - testuser1
    - testuser2
```

А если нам понадобится сделать так, чтобы у каждого пользователя была своя группа, то можно
определить `loop` как список из объектов.

```yaml
- name: Добавление пользователей
  user:
    name: "{{ item.name }}" # <----- подставляется ключ .name из каждого объекта
    state: present
    groups: "{{ item.group }}" # <-- подставляется ключ .group из каждого объекта
  loop:
    - name: testuser1
      group: admin
    - name: testuser2
      group: development
```

`loop` мощная вешь в Ansible и может облегчить многие рутинные процессы. Читайте подробнее про loop
[здесь](https://docs.ansible.com/ansible/latest/user_guide/playbooks_loops.html).

## Шаблоны

Файлы можно копировать на сервер с помощью `copy`, а можно также использовать шаблоны
чтобы генерировать файлы и отправлять их на сервер используя модуль `template`.

Допустим, нам нужно передать в nginx много разных конфигурационных файлов с разными
значениями. Для такой задачи хорошо подходит использовать шаблоны. Шаблоны в Ansible
пишутся в формате [Jinja2][jinja_doc].

Ниже представлен пример шаблона для `server` блоков nginx.

```nginx
server {
    listen {{ server_port }};

    server_name {{ server_name }};

    location / {
        return 200 '{{ hello_message }}';
    }
}
```

Чтобы использовать `template` нужно указать файл шаблона, куда заливать и какие переменные
должны быть переданы в шаблон. В шаблоне выше используются переменные: `server_port`,
`server_name`, `hello_message`.

```yaml
- template:
    src: "./server.conf.j2" # <-- .j2 - это расширение Jinja2
    dest: "/etc/nginx/conf.d/server.conf"
  vars:
    server_port: 8080
    server_name: jusan-template.kz
    hello_message: Hello, from jusan-template example!
```

Теперь, когда будет генерироваться шаблон, наш файл будет иметь следующий вид на сервере:

```nginx
server {
    listen 8080;

    server_name jusan-template.kz;

    location / {
        return 200 'Hello, from jusan-template example!';
    }
}
```

А если вы захотите соединить шаблоны с циклами, то можно сделать так:

```yaml
- template:
    src: "./server.conf.j2"
    dest: "{{ item.dest }}"
  vars:
    server_port: "{{ item.server_port }}"
    server_name: "{{ item.server_name }}"
    hello_message: "{{ item.hello_message }}"
  loop:
    - dest: /etc/nginx/conf.d/server1.conf
      server_port: 8081
      server_name: jusan-template1.kz
      hello_message: Hello, from jusan-template example1!
    - dest: /etc/nginx/conf.d/server2.conf
      server_port: 8082
      server_name: jusan-template2.kz
      hello_message: Hello, from jusan-template example2!
```

В Jinja2 можно делать крутые шаблоны - с условиями, циклами, сложными объектами и т.д.
Подробнее про Jinja2 - [тут][jinja_doc].

[jinja_doc]: https://jinja.palletsprojects.com/en/3.1.x/templates/#synopsis
