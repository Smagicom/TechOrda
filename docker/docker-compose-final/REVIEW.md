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

Перед тем как перейти к данному критерию, удалите все контейнеры на вашей системе.

```bash
docker rm -f $(docker ps -qa)
```

Для проверки заданий в модуле подготовлен тестер. Перед тем как запускать его
нужно выполнить скрипт студента из каждого задания. Склонируйте репозиторий и перейдите в него.

Запустить следующий скрипт. Это запустит все контейнеры из задания.

```bash
cd ./docker-run && bash ./solution.sh && cd ../
cd ./docker-bind && bash ./solution.sh && cd ../
cd ./docker-mount && bash ./solution.sh && cd ../
cd ./dockerfile && bash ./solution.sh && cd ../
cd ./dockerize && bash ./solution.sh && cd ../
cd ./docker-compose && docker compose up -d && cd ../
cd ./docker-compose-final && docker compose up -d && cd ../
```

Теперь нужно запустить `docker-exec`. Откройте файл `docker-exec/solution.sh` и выполните
по одному команды в своем терминале. Нужно по одной линии копировать и вставлять в терминал.

Скачайте [тестер][tester] и запустите его.

[tester]: https://stepik.org/media/attachments/lesson/691221/review-tester.sh

```bash
bash review-tester.sh
```

Должен выйти следующий вывод:

```
docker-run: ✅✅✅
docker-bind: ✅✅✅✅
docker-mount: ✅✅✅✅✅✅
docker-exec: ✅✅✅✅✅✅
dockerfile: ✅✅✅✅✅✅✅
dockerize: ✅✅✅✅✅✅✅
docker-compose: ✅✅✅✅✅✅✅
docker-compose-final: ✅✅✅✅✅✅✅
```

### Критерий оценки #3

Откройте файл `docker-compose/docker-compose.yml`.

Под графой `services` есть только один сервис c названием `api`.

### Критерий оценки #4

Откройте файл `docker-compose-final/docker-compose.yml`.

Под графой `services` есть только два сервиса: `api` и `nginx`.

Сервис `nginx` зависит от сервиса `api`.
