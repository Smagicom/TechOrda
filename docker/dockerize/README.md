# dockerize

В данном задании докеризируем свой проект из задания `jusan-fastapi-final`.

### Полезное

- [FastAPI in Containers](https://fastapi.tiangolo.com/deployment/docker/)
- [Docker Push for Publishing Images](https://www.section.io/engineering-education/docker-push-for-publishing-images-to-docker-hub/)

### Задание

1. Склонируйте содержимое репозитория `jusan-fastapi-final` в репо `jusan-docker/dockerize`.
   Работу будем ввести в нем.
2. Напишите для этого проекта Dockerfile, который запускает API на порту 8080.
3. Произвести сборку образа с именем `jusan-fastapi-final` и тегом `dockerized`.
4. Проверьте на наличие своего образа в вашей системе, перечислите все образы.
5. Запустить контейнер со следующими параметрами:

   - работает на фоне;
   - перенаправляет запрос с хостового порта 8080 на 8080 порт контейнера;
   - имя контейнера `jusan-dockerize`;
   - использует наш собранный образ.

6. Выполненные команды из шагов 3 и 5 записать в файл `dockerize/solution.sh`.
7. Запушить в репозиторий `jusan-docker`. В папке `dockerize` должны быть:
   - получившийся `Dockerfile`.
   - `solution.sh`
   - содержимое репозитория `jusan-fastapi-final`

В репозитории не должно быть лишних файлов.

Для проверки правильности выполнения текущего задания прикреплен [тестер][tester].

```bash
bash ./tester.sh
```

[tester]: https://stepik.org/media/attachments/lesson/691221/tester-dockerize.sh

---

### Ответ


