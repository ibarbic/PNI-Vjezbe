#!C:\Python27\python.exe

import mysql.connector
import json
import password_utils

db_conf = {
    "host":"localhost",
    "db_name": "upload",
    "user":"root",
    "passwd":""
}

def get_DB_connection():
    mydb = mysql.connector.connect(
        host=db_conf["host"],
        user=db_conf["user"],
        passwd=db_conf["passwd"],
        database=db_conf["db_name"]
    )
    return mydb

def create_session():
    query = "INSERT INTO sessions (data) VALUES (%s)"
    values = (json.dumps({}),)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()
    return cursor.lastrowid 

def destroy_session(session_id):
    query = "DELETE FROM sessions WHERE session_id = (%s)"
    values = (session_id,)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()

def get_session(session_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM sessions WHERE session_id=" + str(session_id))
    myresult = cursor.fetchone()
    return myresult[0], json.loads(myresult[1])

def replace_session(session_id, data):#replace-prvo izbrisi, a onda ubaci (delete/insert)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("""
    REPLACE INTO sessions(session_id,data) 
    VALUES (%s,%s)""",
    (session_id, json.dumps(data)))
    mydb.commit()

def create_user(username, password, email, secret_question, secret_answer):
    query = "INSERT INTO users (username, password, email, secret_question, secret_answer) VALUES (%s, %s, %s, %s, %s)"
    hashed_password = password_utils.hash_password(password)
    hashed_secret_answer = password_utils.hash_password(secret_answer)
    values = (username, hashed_password, email, secret_question, hashed_secret_answer) # niz
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    try:
        cursor.execute(query, values)
        mydb.commit()
    except:
        return None
    return cursor.lastrowid 

def get_user(username):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users WHERE username='" + username + "'")
    myresult = cursor.fetchone()
    return myresult

def get_user_by_id(id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users WHERE id="+id)
    myresult = cursor.fetchone()
    return myresult

def get_user_by_email(email):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users WHERE email='" + email + "'")
    myresult = cursor.fetchone()
    return myresult

def update_user_password(username, password):
    hashed_password = password_utils.hash_password(password)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("""
    UPDATE users SET password=%s WHERE username=%s
    """,
    (hashed_password, username))
    mydb.commit()

def create_image(filename, path, generated_name):
    #print(path)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("""
    INSERT INTO image (id, filename, path, counter, created, last, generated_name) VALUES (NULL, '"""+ filename +"""','"""+path+"""', '0', current_timestamp(), current_timestamp(), '"""+ generated_name +"""')
    """)
    mydb.commit()

def get_images():
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM image")
    myresult = cursor.fetchall()
    return myresult

def get_image_by_id(id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM image where id = "+ id )
    myresult = cursor.fetchone()
    return myresult

def delete_image_by_id(id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM image where id = "+ id )
    mydb.commit()

def increase_image_counter_by_id(id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("UPDATE image SET counter = counter + 1 where id = "+ id )
    mydb.commit()