import uvicorn
from fastapi import FastAPI
import applibrary as lib

# Global variable so Uvicorn can find it
app = FastAPI()

@app.get("/")
def default():
    return {"message": "Yahoo!! The server is Alive."}

@app.get("/fib/{n}")
def fib(n:int):
    return {"fib": f"{lib.fib(n)}"}


# The wrapper function your package tool will call
def start():
    uvicorn.run("fastapiserver.main:app", host="127.0.0.1", port=8000, reload=True)

if __name__ == "__main__":
    start()


        