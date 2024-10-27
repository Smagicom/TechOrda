# dockerfile

В данном задании научимся собирать свой образ с приложением с помощью Dockerfile.

Dockerfile - это файл, описывающий команды сборки образа контейнера.

### Полезное

- [Изучаем Docker: файлы Dockerfile](https://habr.com/ru/company/ruvds/blog/439980/)
- [Dockerfile Tutorial](https://docker-curriculum.com/#dockerfile)

### Задание

1. Вся работа должна выполняться в репозитории `jusan-docker` в папке `dockerfile`.
2. Скачать конфигурационный файл [jusan-dockerfile.conf][jusan-dockerfile-conf] с помощью `curl`.
3. Скачать конфигурационный файл [jusan-dockerfile.zip][jusan-dockerfile-zip] с помощью `curl`.
   Разархивировать архив с помощью `unzip`.
4. Создать Dockerfile, который:

   - использует базовый образ `nginx:mainline`;
   - копирует `jusan-dockerfile.conf` в `/etc/nginx/conf.d/jusan-dockerfile.conf`
   - копирует распакованный `jusan-dockerfile.zip`. Определите куда нужно монтировать по конфигурационному файлу.

5. Произвести сборку образа с именем `nginx` и тегом `jusan-dockerfile`.
6. Проверьте на наличие своего образа в вашей системе, перечислите все образы `docker images`.
7. Запустить контейнер со следующими параметрами:

   - работает на фоне;
   - перенаправляет запрос с хостового порта 6060 на 80 порт контейнера;
   - имя контейнера `jusan-dockerfile`;
   - использует наш собранный образ.

8. Проверьте запросы с помощью `curl`:

   - `http://localhost:6060` - ожидаемый ответ: `<h1>Hello, from jusan-dockerfile!</h1>`;
   - `http://localhost:6060/dockerfile` - ожидаемый ответ: `FROM nginx:mainline`;
   - `http://localhost:6060/secret` - ожидаемый ответ: `jusan-dockerfile`;
   - `http://localhost:6060/jusan` - ожидаемый ответ: `singularity`;

9. Команды из шагов 2, 3, 5, 7 записать в файл `dockerfile/solution.sh`.
10. Запушить в репозиторий `jusan-docker`. В папке `dockerfile` должны быть:
    - получившийся `Dockerfile`.
    - `solution.sh`

В репозитории не должно быть лишних файлов.

Для проверки правильности выполнения текущего задания прикреплен [тестер][tester].

```bash
bash ./tester.sh
```

[jusan-dockerfile-conf]: https://stepik.org/media/attachments/lesson/686238/jusan-dockerfile.conf
[jusan-dockerfile-zip]: https://stepik.org/media/attachments/lesson/686238/jusan-dockerfile.zip
[tester]: https://stepik.org/media/attachments/lesson/691221/tester-dockerfile.sh

---

### Ответ
