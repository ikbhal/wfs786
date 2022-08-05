import sqlite3

def connect_to_db():
    conn = sqlite3.connect('wf.db')
    return conn

def get_users_from_db():
    print("inside ikb: get_users_from_db ")
    users = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()

        # convert row objects to dictionary
        for i in rows:
            user = {}
            user["id"] = i["id"]
            user["email"] = i["email"]
            user["password"] = i["password"]
            user["mobile_number"] = i["mobile_number"]
            
            users.append(user)

    except:
        users = []

    return users


def get_user_by_email_and_password(email, password):
    print("ikb> get_user_by_email_and_password :", email, ", password:", password)
    user = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE email = ? and password=?", 
                       (email, password))
        row = cur.fetchone()

        # convert row object to dictionary
        user["id"] = row["id"]
        user["email"] = row["email"]
        # user["password"] = row["password"]
        user["mobile_number"] = row["mobile_number"]
    except:
        user = {}

    return user

def get_user_by_id(user_id):
    print("ikb > get_user_by_id :", user_id)
    user = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE id = ?", 
                       (user_id,))
        row = cur.fetchone()

        # convert row object to dictionary
        user["id"] = row["id"]
        user["email"] = row["email"]
        # user["password"] = row["password"]
        user["mobile_number"] = row["mobile_number"]
    except:
        user = {}

    return user


def insert_user(user):
    inserted_user = {}
    print("ikb  ...insert user ", user)

    # return node
    conn = sqlite3.connect('wf.db')
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO users (id, email, password, mobile_number) VALUES (?, ?, ?, ?)",
                    (user['id'],   
                    user['email'],   
                    user['password'],
                    user['mobile_number']) )
        conn.commit()
        inserted_user = get_user_by_id(user['id'])
    except Exception as e:
        conn.rollback()
        print("exception error: {0}".format(e))

    finally:
        conn.close()

    return inserted_user