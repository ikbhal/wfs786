from flask import Flask,jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'web app with Python Flask'

@app.route('/load')
def load():
    data = [
        {
            'id': 1,
            'title': 'n1',
            'childrenIds':[2,3,4]
        },
        {   
            'id':2,
            'title': 'n2',
            'childrenIds':[]
        },
        {   
            'id':3,
            'title': 'n3',
            'childrenIds':[]
        }
    ]
    return jsonify(data);


@app.route('/save', methods=['POST'])
def save():
    content_type = request.headers.get('Content-Type', 'application/json')
    if (content_type == 'application/json'):
        json = request.json
        return json 
    else:
        return 'Cont-Type not supported!'



app.run(host='0.0.0.0', port=81)