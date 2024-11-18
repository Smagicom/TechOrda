# pgsql-commands

Команда `psql` — это CLI-программа, которая поставляется с каждой установкой PostgreSQL.
Базовые знания `psql` обязательны для администрирования postgres.
`psql` обеспечивает доступ к postgres кластеру.

psql поддерживает несколько флагов подключения к базе данных:

- `-d` название базы данных
- `-U` логин пользователя
- `-h` хост базы данных, т.е. ip-адрес

Если флаги не указаны, psql предполагает, что вы пытаетесь подключиться с именем своей учетной записи пользователя.
То есть, если у вас логин пользователя `root`, то вводя `psql` - это эквивалентно `psql -U root`.

```bash
$ sudo -iu postgres psql
psql (14.2 (Ubuntu 14.2-1.pgdg18.04+1))
Type "help" for help.
postgres=#
```

Кусок команды `sudo -iu postgres` значит, чтобы команда `psql` была запущена через пользователя `postgres`.
Попробуйте запустить без этого куска `psql`:

```bash
$ psql
psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: FATAL:  role "root" does not exist
```

Вышла ошибка, обозначающая что пользователь `root` не существует в базе данных `postgres`. Чтобы исправить эту ошибку нужно
создать пользователя `root` и добавить права в конфигурацию чтобы разрешить подключаться - это объясним позже.

Чтобы выйти из `psql` и закрыть соединение с базой данных, вы должны ввести `\q` или `quit` и нажать `Enter` (вы также можете нажать `CTRL + D` для выхода).

## Команды psql

Каждая команда, относящаяся к psql, начинается с символа обратной косой черты `\`. Можно получить некоторую справку об SQL операциях и командах PostgreSQL с помощью специальной команды `\h`, после чего вы можете указать конкретную команду, для которого вам нужна справка:

```
postgres=# \h SELECT
```

Покажет документацию команды `SELECT`:

```
Command: SELECT
Description: retrieve rows from a table or view Syntax:
[ WITH [ RECURSIVE ] with_query [, ...] ]
SELECT [ ALL | DISTINCT [ ON ( expression [, ...] ) ] ]
       [ * | expression [ [ AS ] output_name ] [, ...] ]
   ...
   URL: https://www.postgresql.org/docs/12/sql-select.html
```

Если нужна справка команд psql, можете ввести команду `\?`:

```
postgres=# \?
```

```
General
  \copyright             show PostgreSQL usage and distribution terms
  \crosstabview [COLUMNS] execute query and display results in crosstab
  \errverbose            show most recent error message at maximum verbosity
  \g [(OPTIONS)] [FILE]  execute query (and send results to file or |pipe);
```

Эти команды полезны для получения представления о том, какие объекты определены в текущей базе данных.

### \du - describe users

Получение информации о существующих пользователях и их свойствах очень полезно. psql предоставляет специальную команду `\du` (describe users) для вывода списка всех доступных пользователей (ролей) в системе:

```
postgres=# \du
```

```
                                   List of roles
 Role name |                         Attributes                         | Member of
-----------+------------------------------------------------------------+-----------
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
```

### \dt - describe tables

Чтобы получиться список всех таблиц в текущей базе данных нужно ввести команду `\dt` (describe tables).

```
postgres=# \dt
```

```
         List of relations
 Schema | Name  | Type  |  Owner
--------+-------+-------+----------
 public | users | table | postgres
```

### \l - list databases

Чтобы получить список всех баз данных в `postgres` нужно ввести `\l` (list databases).

```
postgres=# \l
```

```
                              List of databases
   Name    |  Owner   | Encoding | Collate |  Ctype  |   Access privileges
-----------+----------+----------+---------+---------+-----------------------
 postgres  | postgres | UTF8     | C.UTF-8 | C.UTF-8 |
 template0 | postgres | UTF8     | C.UTF-8 | C.UTF-8 | =c/postgres          +
           |          |          |         |         | postgres=CTc/postgres
 template1 | postgres | UTF8     | C.UTF-8 | C.UTF-8 | =c/postgres          +
           |          |          |         |         | postgres=CTc/postgres
(3 rows)
```

Также, чтобы получить более расширенную информацию о базах данных есть команда `\l+`, которая
также покажет размер базы данных.

```
postgres=# \l+
```

```
                                                                List of databases
   Name    |  Owner   | Encoding | Collate |  Ctype  |   Access privileges   |  Size   | Tablespace |                Description
-----------+----------+----------+---------+---------+-----------------------+---------+------------+--------------------------------------------
 postgres  | postgres | UTF8     | C.UTF-8 | C.UTF-8 |                       | 8585 kB | pg_default | default administrative connection database
 template0 | postgres | UTF8     | C.UTF-8 | C.UTF-8 | =c/postgres          +| 8369 kB | pg_default | unmodifiable empty database
           |          |          |         |         | postgres=CTc/postgres |         |            |
 template1 | postgres | UTF8     | C.UTF-8 | C.UTF-8 | =c/postgres          +| 8521 kB | pg_default | default template for new databases
           |          |          |         |         | postgres=CTc/postgres |         |            |
(3 rows)
```

Однако, таблица выше имеет много колонок и может не вмещаться на экране. Для удобства вывода
есть команда `\x` (expanded output), которая выведет колонки таблицы на отдельных линиях.

```
postgres=# \x
Expanded display is on.
postgres=# \l+
```

```
List of databases
-[ RECORD 1 ]-----+-------------------------------------------
Name              | postgres
Owner             | postgres
Encoding          | UTF8
Collate           | C.UTF-8
Ctype             | C.UTF-8
Access privileges |
Size              | 8585 kB
Tablespace        | pg_default
Description       | default administrative connection database
-[ RECORD 2 ]-----+-------------------------------------------
Name              | template0
Owner             | postgres
Encoding          | UTF8
Collate           | C.UTF-8
Ctype             | C.UTF-8
Access privileges | =c/postgres                               +
                  | postgres=CTc/postgres
Size              | 8369 kB
Tablespace        | pg_default
Description       | unmodifiable empty database
-[ RECORD 3 ]-----+-------------------------------------------
Name              | template1
Owner             | postgres
Encoding          | UTF8
Collate           | C.UTF-8
Ctype             | C.UTF-8
Access privileges | =c/postgres                               +
                  | postgres=CTc/postgres
Size              | 8521 kB
Tablespace        | pg_default
Description       | default template for new databases
```

### \c - connect

PostgreSQL может содержать несколько баз данных. Для того, чтобы перейти в содержимое одной из баз данных
нужно к ней подключиться - `\c` (connect).

```
postgres=# \c template1
You are now connected to database "template1" as user "postgres".
```

У каждой базы данных есть свои таблицы, так что можете ввести `\dt`, чтобы посмотреть на них.

### \d+ table_name

Каждая таблица содержит колонки с разными типами данных. На эти колонки могут быть наложены индексы, foreign ключи и т.д.

Для подробной информации о конкретной таблице введите `\d+ название_таблицы`.

```
postgres=# \d+ users
```

```
                                                       Table "public.users"
 Column |  Type   | Collation | Nullable |              Default              | Storage | Compression | Stats target | Description
--------+---------+-----------+----------+-----------------------------------+---------+-------------+--------------+-------------
 id     | integer |           | not null | nextval('users_id_seq'::regclass) | plain   |             |              |
Indexes:
    "users_pkey" PRIMARY KEY, btree (id)
Access method: heap
```

Поздравляем! Вы научились основным командам psql, которые помогут получить представление о базе данных и таблицах.
Этот навык будет очень полезным для диагностики и нахождения проблем.

В текущем задании можете просто запустить сервер, на котором запущен postgres и нажать "Отправить".
Подробные задания описаны в следующих шагах.
