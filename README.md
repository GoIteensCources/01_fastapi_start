# Learning FastAPI 

FastAPI — це сучасний, швидкий, асинхронний (високопродуктивний) веб-фреймворк для побудови API з Python 3.7+, базуючись на стандартних типах Python

## Dependency

```bash 
pip install -f requrements.txt
```


## Documentation

fastapi: https://fastapi.tiangolo.com/uk/

uvicorn:    https://www.uvicorn.org/

HTTPX: https://www.python-httpx.org/quickstart/


## Example
Створення доданку FastAPI. Зазвичай створюється у файлі "main.py"

```python3
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
```
Запуск сервера

```bash
uvicorn main:app --reload --host localhost --port 8000
``` 

## Auto documentation API
http://127.0.0.1:8000/docs

http://127.0.0.1:8000/redoc

