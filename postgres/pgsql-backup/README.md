# pgsql-backup

Неважно, насколько надежно ваше аппаратное и программное обеспечение — рано или поздно вам потребуется вернуться в прошлое, чтобы восстановить случайно удаленные или поврежденные данные. Это цель бэкапов — копии, которые вы можете хранить в течение определенного периода времени, что позволяет вам восстановить данные даже в случае потери.

В создании бэкапов задействована CLI-команда — `pg_dump`.

- pg_dump используется для создания дампа одной базы данных в кластере.

## pg_dump

По умолчанию `pg_dump` использует простой текстовый формат, который создает SQL команды, которые можно использовать для восстановления структуры и содержимого базы данных и выводит резервную копию на стандартный вывод.
Это означает, что если вы создадите бэкап базы данных без использования каких-либо флагов, вы увидите длинный список SQL операции:

```
pg_dump -U postgres deadline
```

```sql
--
-- PostgreSQL database dump
--

-- Dumped from database version 14.2 (Debian 14.2-1.pgdg110+1)
-- Dumped by pg_dump version 14.2 (Debian 14.2-1.pgdg110+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;

-- Name: deadline; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.deadline (
    id integer NOT NULL,
    name character varying,
    duration interval,
    deadline_type_id integer NOT NULL,
    attrs jsonb,
    created_at timestamp without time zone DEFAULT now(),
    updated_at timestamp without time zone DEFAULT now()
);

--- ...
```

Есть два способа сохранить вывод `pg_dump` в файл. Первый - это перенаправить вывод в файл, как показано в следующем примере:

```bash
pg_dump -U postgres deadline > backup_deadline.sql
```

Другой способ — использовать параметр `pg_dump -f`, который позволяет указать имя файла, в который будет помещено содержимое. Здесь предыдущую командную строку можно переписать следующим образом:

```bash
pg_dump -U postgres -f backup_deadline.sql deadline
```

## Восстановление бэкапа

Бэкап файл `backup_deadline.sql` не будет содержать инструкций по созданию новой базы данных.
Это может быть удобно, но также и опасно: это означает, что восстановление будет происходить в базе данных, к которой вы подключены.

Давайте предположим, что мы хотим восстановить содержимое базы данных в другую локальную базу данных, которую мы собираемся назвать `deadline_test`.
Первым шагом является создание базы данных следующим образом:

```
$ psql -U postgres template1
template1=# CREATE DATABASE deadline_test;
CREATE DATABASE
```

Теперь можно подключиться к базе данных `deadline_test` и выполнить операции по восстановлению из бэкапа:

```
psql -U postgres deadline_test < ./backup_deadline.sql
```

### Задание

1. На сервере установлен `postgres`. В ней создана база данных `deadline`.
2. Создайте бэкап базы данных `deadline` в файл `/home/box/backup_deadline.sql`.
3. Восстановите `/home/box/backup_deadline.sql` в базу данных `deadline_test`.

---

### Ответ
