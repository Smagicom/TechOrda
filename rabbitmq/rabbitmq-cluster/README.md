# rabbitmq-cluster

### Полезное

- [RabbitMQ Clustering](https://www.rabbitmq.com/clustering.html)

### Задание

1. Пройти по ссылке задания в GitHub Classroom
   
   Задание выполняется в GitHub Classroom. После выполнения пришлите свою ссылку на рецензию ревьюеру в Stepik ([ССЫЛКА GITHUB CLASSROOM]).
2. Создайте скрипт `setup.sh`, который:
   - создаст кластер RabbitMQ из 2 контейнеров
   - каждый MongoDB контейнер использует образ `rabbitmq:3.9-management`.
   - назовите каждый контейнер `rabbit-1`, `rabbit-2`
   - `rabbit-1` имеет порты `5672:5672`, `15672:15672`.
   - `rabbit-2` имеет порты `5673:5672`, `15673:15672`.
   - объедините `rabbit-2` в один кластер с `rabbit-1`
3. Запушить все необходимые файлы в репо `jusan-rabbitmq`.

---

### Ответ

- [setup.sh](./setup.sh)
