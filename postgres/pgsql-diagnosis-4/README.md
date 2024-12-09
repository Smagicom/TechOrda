# pgsql-diagnosis-4

### Задание

1. Пришлите названия колонок через новую линию в БД `deadline` в таблице `student_deadline` на сервере `pgsql-commands` в `postgres`.

---

### Ответ

```SQL
SELECT column_name 
FROM information_schema.columns 
WHERE table_name = 'student_deadline';


```