# docker-run

Задания в данном модуле будут проверяться ментором в конце модуля.

Для сдачи данного модуля создайте репозиторий в ([ССЫЛКА GITHUB CLASSROOM]).

### Полезное

- [Установка Docker](https://docs.docker.com/get-docker/)

### Задание

1. Установить Docker, если еще не установлен на вашем компьютере.
2. Запустить контейнер на порту `8888` из официального образа `nginx`:

```bash
docker run -d --name jsn-dkr-run -p 8888:80 nginx:mainline
```

3. Вывести список активных контейнеров:

```bash
docker ps
```

4. Проверьте запрос на `http://localhost:8888` с помощью `curl`. Должно появиться приветственное сообщение от `nginx`.
5. Остановить запущенный контейнер:

```bash
docker stop jsn-dkr-run
```

6. Вывести список активных контейнеров, чтобы убедиться что нашего контейнера нет в списке.
7. Проверьте запрос `http://localhost:8888` с помощью `curl`. Должна появиться ошибка, так как наш контейнер был остановлен.
8. Вывести список всех контейнеров. В нем должен появиться наш остановленный контейнер.

```bash
docker ps -a
```

9. Все выполенные команды `docker` записать в репозиторий в файл `docker-run/solution.sh`. В скрипте не должно быть команд `curl`.
   Запушить в гит.

В репозитории не должно быть лишних файлов.

Для проверки правильности выполнения текущего задания прикреплен [тестер][tester].

```bash
bash ./tester.sh
```

[tester]: https://stepik.org/media/attachments/lesson/691221/tester-docker-run.sh

---

### Ответ
sudo docker run -d --name jsn-dkr-run -p 8887:80 nginx:mainline
8e2cfdffa414de0acda7dc746ca3a0c1656c7d130269853e932a324f8a4348e9

 sudo docker ps
8e2cfdffa414   nginx:mainline              "/docker-entrypoint.…"   6 minutes ago   Up 6 minutes    0.0.0.0:8887->80/tcp, [::]:8887->80/tcp

sudo docker stop jsn-dkr-run

sudo docker ps -a



