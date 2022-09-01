from config import app 
from asynctasks import invoke

@app.get("/hello")
def hello():
    return "Flass app is running!!! Hello !!!!"

@app.get("/greet")
def greet():
    return "Hey! How are you"

@app.get("/invoke-tasks")
def invoketask():
    invoke()
    return "Task has been initiated nothing to worry"