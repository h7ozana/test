from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'ohcloud 20240121'
