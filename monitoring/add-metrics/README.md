# add-metrics

Проект данного модуля состоит из двух частей и проверяется в конце ментором. Это первая часть проекта. Сделав это задание, переходите к следующему.

В данном задании мы узнаем как пишутся метрики и что они из себя представляют на деле.

### Полезное

- [Prometheus Python Client](https://github.com/prometheus/client_python)
- [FastAPI + Prometheus exporter][make_asgi_app]

[make_asgi_app]: https://github.com/prometheus/client_python/pull/512#issuecomment-591866511

### Задание

1.  В своем раннее созданном репозитории `jusan-fastapi-final` создайте ветку `monitoring`.
    Текущее задание должно выполняться на данной ветке.
2.  Создайте следующие метрики:

    - Метрика типа Counter с названием `http_requests_total`, описанием `Number of HTTP requests received` и
      параметрами `method` и `endpoint`. В `endpoint` должен храниться путь, например `/sum1n`, в `method` - HTTP метод.
      Метрика должна показывать кол-во запросов на каждый роут и метод;
    - Метрика типа Histogram с названием `http_requests_milliseconds`, описанием `Duration of HTTP requests in milliseconds` и
      параметрами `method` и `endpoint`. Метрика должна отображать длительность в миллисекундах на каждый роут и метод;
    - Метрика типа Gauge с названием `last_sum1n` и описанием `Value stores last result of sum1n`;
      Метрика должна показывать последний результат от `sum1n`;
    - Метрика типа Gauge с названием `last_fibo` и описанием `Value stores last result of fibo`;
      Метрика должна показывать последний результат от `fibo`;
    - Метрика типа Gauge с названием `list_size` и описанием `Value stores current list size`;
      Метрика должна показывать последний результат от `size`;
    - Метрика типа Gauge с названием `last_calculator` и описанием `Value stores last result of calculator`;
      Метрика должна показывать последний результат от `calculator`;
    - Метрика типа Counter с названием `errors_calculator_total` и описанием `Number of errors in calculator`;
      Метрика должна показывать кол-во ошибок в `calculator` - например невалидный формат, zerodiv и т.д.

3.  Настроить экспортер по роуту `/metrics` - [подсказка][make_asgi_app].
4.  Запустите API и зайдите на страницу `/metrics` - посмотрите что отображает экспортер.
5.  Сделайте несколько запросов на разные роуты у API, снова зайдите на страницу экспортера -
    проверьте обновились ли метрики.
6.  Запушить изменения в гит.

---

### Ответ

