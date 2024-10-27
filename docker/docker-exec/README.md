# docker-exec

### Задание

1. Вся работа должна выполняться в репозитории `jusan-docker` в папке `docker-exec`.
2. Запустить контейнер со следующими параметрами:

   - работает на фоне;
   - перенаправляет запрос с хостового порта 8181 на 80 порт контейнера;
   - имя контейнера `jusan-docker-exec`;
   - использует образ `nginx:mainline`.

3. Зайти в терминал контейнера `jusan-docker-exec`.
4. Создать новый конфигурационный файл для nginx.

```bash
cat << EOF > /etc/nginx/conf.d/jusan-docker-exec.conf
server {
    listen 80;
    server_name jusan.singularity;

    location / {return 200 'Hello, from jusan-docker-exec';}
    location /home {return 201 'This is my home!';}
    location /about {return 202 'I am just an exercise!';}
}
EOF
```

5. Перезагрузите nginx внутри контейнера.
6. Выйти из терминала контейнера
7. Проверьте запросы с помощью `curl`:

   - `http://localhost:8181` - ожидаемый ответ: `Hello, from jusan-docker-exec`;
   - `http://localhost:8181/home` - ожидаемый ответ: `This is my home!`;
   - `http://localhost:8181/about` - ожидаемый ответ: `I am just an exercise!`;

8. Посмотрите на логи `nginx`:

```bash
docker logs jusan-docker-exec
```

7. Все выполненные команды начиная со 2 шага, кроме 7 и 8, записать в файл `docker-exec/solution.sh`.
8. Запушить в репозиторий `jusan-docker`. В папке `docker-exec` должны быть:
   - `solution.sh`

В репозитории не должно быть лишних файлов.

Для проверки правильности выполнения текущего задания прикреплен [тестер][tester].

```bash
bash ./tester.sh
```

[tester]: https://stepik.org/media/attachments/lesson/691221/tester-docker-exec.sh

---

### Ответ
