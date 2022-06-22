from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World by Flask - Testing", 200

app.run()