from flask import Flask
app = Flask(__name__)

def hello():
    return "test!"

def hello1():
    return "Hello World!"

@app.route("/")
def hello1():
    return "Hello World!"

if __name__ == "__main__":
    app.run()