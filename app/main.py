from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    for i in range(10):
        print(i)
    return {"Hello": "World"}
