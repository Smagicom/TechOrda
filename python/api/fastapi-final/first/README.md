# FAST API PROJECT
Fast Api проект 

С начала нужно активировать окружение и скачать нужные библотеки что бы проект запускалась
Для Windows:

```bash
python -m venv venv
```
Затем активируйте его командой:
```bash
venv\Scripts\activate
```

Для macOS/Linux:
```bash
python3 -m venv venv
```

Активация окружения:
```bash
source venv/bin/activate
```

### Скачать необхадимые библотеки

FastApi, Uvicorn

```bash
pip install "fastapi" "uvicorn[standard]"
```

Запуск проекта
```bash
curl http://127.0.0.1:8000/
```

Проверьте автоматически созданную [документацию](http://127.0.0.1:8000/docs).


