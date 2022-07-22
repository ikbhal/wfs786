from flask import Flask,jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'web app with Python Flask'

@app.route('/load')
def load():
    return jsonify('load');

@app.route('/save', methods=['POST'])
def save():
    node = request.json
    return jsonify(node);

@app.route('/nodes', methods=['POST'])
def createNode():
    print("create node")
    node = request.json
    return jsonify(node);

app.run(host='0.0.0.0', port=81, debug=True)

#app.run(debug=True)