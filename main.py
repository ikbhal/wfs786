from flask import Flask,jsonify, request
from flask_cors import CORS, cross_origin
import sqlite3

app = Flask(__name__)
CORS(app, support_credentials=True)

def connect_to_db():
    conn = sqlite3.connect('wf.db')
    return conn

def get_nodes_from_db():
    print("inside ikb: get_users ")
    nodes = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM nodes")
        rows = cur.fetchall()

        # convert row objects to dictionary
        for i in rows:
            node = {}
            node["id"] = i["id"]
            node["text"] = i["text"]
            node["childrenIds"] = i["childrenIds"]
            
            nodes.append(node)

    except:
        nodes = []

    return nodes

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



def update_node_in_db(node):
    print("inside update node helper db method", node)
    updated_node = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("UPDATE nodes SET text = ?, childrenIds = ? WHERE id =?",  
                     (node["text"], node["childrenIds"], node["id"],))
        conn.commit()
        #return the user
        updated_node = get_node_by_id(node["id"])

    except Exception as e:
        # print("error during update ", e)
        print("exception error: {0}".format(e))
        conn.rollback()
        updated_node = {}
    finally:
        cur.close() 
        conn.close()

    return updated_node

@app.route('/')
def index():
    return 'web app with Python Flask'

@app.route('/load')
def load():
    nodes = get_nodes_from_db()
    res = {
        "nodes": nodes,
        "startNodeId": 1, 
        "nodeIdLast": len(nodes)
    }
   
    return jsonify(res)

@app.route('/save', methods=['POST'])
def save():
    print("ikb reach save api")
    # nodeDb= insert_node(nodeReq)
    return jsonify(" will work soon")

@app.route('/nodes')
def get_nodes():

    rows = get_nodes_from_db()
    return jsonify(rows)
    # return jsonify([{"id":1, "text":"text", "childrenIds":[]}])

@app.route('/nodes', methods=['POST'])
def createNode():
    print("create node")
    # node = request.json
    nodeReq = request.json
    print("nodeReq:", nodeReq)
    nodeDb= insert_node(nodeReq)
    # return jsonify(nodeDb)
    return jsonify(nodeReq)

@app.route('/nodes', methods=['PUT'])
def update_node():
    print("ikb inside update_node ")
    node = request.json
    node_db= update_node_in_db(node)
    print("update node from db is ", node_db)
    # return jsonify(node_db)
    return jsonify(node_db)

app.run(host='0.0.0.0', port=81, debug=True)

#app.run(debug=True)