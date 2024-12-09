# pgsql-pgtune

PostgreSQL, как и nginx, имеет основной файл конфигурации, который отвечает
за внутренние параметры сервиса. Этих переменных очень много и уметь их
правильно настраивать под свои нужды является отдельным искуством.

Есть хороший ресурс [pgtune.leopard.in.ua](https://pgtune.leopard.in.ua/),
который подбирает оптимальные параметры конфигурации для того чтобы оптимизировать
базу данных под характеристики сервера, сложности и частоты запросов.

### Задание

1. Подберите параметры на [pgtune.leopard.in.ua](https://pgtune.leopard.in.ua/) под характеристики:
   - PostgreSQL 14
   - ОС: Linux
   - Тип БД: Обработка онлайн-транзакций
   - ОЗУ: 512 MB
   - ЦПУ: 2
   - Тип хранилища: SSD
2. Пришлите получившийся конфиг.

---

### Ответ
# DB Version: 17
# OS Type: linux
# DB Type: web
# Total Memory (RAM): 512 MB
# CPUs num: 2
# Connections num: 20
# Data Storage: ssd

max_connections = 20
shared_buffers = 128MB
effective_cache_size = 384MB
maintenance_work_mem = 32MB
checkpoint_completion_target = 0.9
wal_buffers = 3932kB
default_statistics_target = 100
random_page_cost = 1.1
effective_io_concurrency = 200
work_mem = 3276kB
huge_pages = off
min_wal_size = 1GB
max_wal_size = 4GB