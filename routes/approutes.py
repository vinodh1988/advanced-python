from config import app 


@app.get("/hello")
def hello():
    return "Flass app is running!!! Hello !!!!"