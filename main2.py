from flask import Flask,jsonify, request
import sqlite3

app = Flask(__name__)

def connect_to_db():
    conn = sqlite3.connect('wf.db')
    return conn

def insert_node(node):
    inserted_node = {}
    print("ikb  ...node")
    print(node)

    # return node
    conn = sqlite3.connect('wf.db')
    try:
        # conn = connect_to_db()
       
        cur = conn.cursor()
        cur.execute("INSERT INTO nodes (id, text, childrenIds) VALUES (?, ?, ?)",
        # cur.execute("INSERT INTO nodes (id, text, childrenIds) VALUES (10, 'n1', '')")
                    (node['id'],   
                    node['text'],   
                    node['childrenIds']) )

        # cur.execute("INSERT INTO nodes VALUES(7,'n7','')")
        conn.commit()
        # inserted_node = get_node_by_id(node['id'])
    except Exception as e:
        conn.rollback()
        print("exception error: {0}".format(e))

    finally:
        conn.close()

    return node

def get_node_by_id(node_id):
    node = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM nodes WHERE id = ?", 
                       (node_id,))
        row = cur.fetchone()

        # convert row object to dictionary
        node["id"] = row["id"]
        node["text"] = row["text"]
        node["childrenIds"] = row["childrenIds"]
    except:
        node = {}

    return node


@app.route('/')
def index():
    return 'web app with Python Flask'

@app.route('/load')
def load():
    return jsonify('load');

@app.route('/save', methods=['POST'])
def save():
    print("ikb reach save api")
    # nodeDb= insert_node(nodeReq)
    return jsonify(" will work soon")

@app.route('/nodes', methods=['POST'])
def createNode():
    print("create node")
    # node = request.json
    nodeReq = request.json
    print("nodeReq:", nodeReq)
    nodeDb= insert_node(nodeReq)
    # return jsonify(nodeDb)
    return jsonify(nodeReq)

app.run(host='0.0.0.0', port=81, debug=True)

#app.run(debug=True)