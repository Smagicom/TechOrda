# fastapi-final

В этом задании придется решать задачи из Java Интенсива, но на Python. На Java Интенсиве вы уже изучили основы программирования, поэтому для вас не составит труда ознакомиться с основами Python.

Если у вас все же возникнут сложности с Python, не переживайте - это нормально. Советуем активно использовать Google для освоения Python.

В этом задании разрешается использовать все встроенные библиотеки Python.

### Полезные ссылки

- [Postman.com](https://www.postman.com/)
- [Postman API testing](https://www.postman.com/automated-testing/)
- [FastAPI туториал](https://fastapi.tiangolo.com/tutorial/)

### Задание

#### 1. Пройти по ссылке задания в GitHub Classroom

Задание выполняется в GitHub Classroom. После выполнения пришлите свою ссылку на рецензию ревьюеру в Stepik ([ССЫЛКА GITHUB CLASSROOM])

#### 2. Создать роуты.

`/sum1n`, принимающий GET запросы.

Передается число n через URL. Вернуть сумму от 1 до n.

Пример запроса.

```bash
$ curl http://localhost:8000/sum1n/10
{"result": 55}
```

---

`/fibo`, принимающий GET запросы.

Передается число n через URL Query. Вернуть n-ное число из последовательности Фибоначчи.

Пример запроса.

```bash
$ curl http://localhost:8000/fibo?n=5
{"result": 3}
```

---

`/reverse`, принимающий POST запросы.

Передается строка `string` через Header. Вернуть перевернутую строку задом наперед.

Пример запроса.

```bash
$ curl -X POST -H "string: hello" http://localhost:8000/reverse
{"result": "olleh"}
```

---

`/list`, принимающий PUT запросы.

Передается строка `element` через JSON тело запроса. Сохранить строку `element` в глобальный массив.

Пример запроса.

```bash
$ curl -X PUT -d '{"element":"Apple"}' -H 'Content-Type: application/json' http://localhost:8000/list
$ curl -X PUT -d '{"element":"Microsoft"}' -H 'Content-Type: application/json' http://localhost:8000/list
$ curl http://localhost:8000/list
{"result": ["Apple", "Microsoft"]}
```

---

`/list`, принимающий GET запросы.

Вернуть глобальный массив.

Пример запроса.

```bash
$ curl http://localhost:8000/list
{"result": []}
$ curl -X PUT -d '{"element":"Apple"}' -H 'Content-Type: application/json' http://localhost:8000/list
$ curl -X PUT -d '{"element":"Microsoft"}' -H 'Content-Type: application/json' http://localhost:8000/list
$ curl http://localhost:8000/list
{"result": ["Apple", "Microsoft"]}
```

---

`/calculator`, принимающий POST запросы.

Передается строка `expr` через JSON тело запроса. Строка `expr` состоит из математического выражения, которое нужно вычислить. Формат строки следующий: `num1,operator,num2`.

- `num1` и `num2` - это числа
- `operator` - это математическая операция: +,-,/,\*

Вернуть результат математического выражения.

Если `expr` неверного формата, вернуть `{"error": "invalid"}` со статусом `400 Bad Request`.

При делении на ноль вернуть `{"error": "zerodiv"}` со статусом `403`.

Пример запроса.

```bash
$ curl -X POST -d '{"expr": "1,+,1"}' -H 'Content-Type: application/json' http://localhost:8000/calculator
{"result": 2}
```

#### 3. Создать файл зависимостей и добавить его в репозиторий.

```bash
pip freeze > requirements.txt
```

#### 4. Написать в `README.md` инструкцию для запуска проекта, начиная с установки окружения и установки зависимостей pip.

#### 5. Добавить файл .gitignore, который содержит [рекомендации](https://github.com/github/gitignore/blob/main/Python.gitignore).

#### 6. Установить Postman.

#### 7. Для каждого роута написать unit-тест на проверку статус кода. Название каждого запроса в Postman должно четко отражать его цель.

#### 8. Экспортировать коллекцию и добавить файл с тестами в репозиторий.

#### 9. Отправить изменения в github.com - `git push`.

#### 10. Прислать ссылку на созданный репозиторий.
