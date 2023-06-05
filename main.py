from fastapi import FastAPI
from secrets import choice
from jokes_API import  joke_catch
import string
import uvicorn
import json

app = FastAPI()


@app.get("/hello")
@app.get("/hello/")
def hello_road():
    return json.dumps({''.join([choice(string.ascii_uppercase + string.digits) for _ in range(6)]): "Hello, World!"})


@app.get("/health/readiness")
@app.get("/health/liveness")
def status_road():
    return json.dumps({"status": "UP"})


@app.get("/joke")
def joke_road():
    return json.dumps(joke_catch())


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8091, reload=True)
