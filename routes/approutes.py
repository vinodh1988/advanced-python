from config import app 


@app.get("/hello")
def hello():
    return "Flass app is running!!! Hello !!!!"

@app.get("/greet")
def greet():
    return "Hey! How are you"