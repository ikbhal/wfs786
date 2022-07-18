from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'web app with Python Flask'

app.run(host='0.0.0.0', port=81)