#!C:\Python27\python.exe

import base
import os
import cgi
import session
import auth


def print_login_form():
    print ('''
        <form method="POST">
            username <input type="text" name="username" />
            password <input type="password" name="password"/>
            <input type="submit" value="Login"/>
            <br>
            <br>
            <a href='register.py'>Register</a>
        </form>
    ''')

params = cgi.FieldStorage()
if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    username = params.getvalue("username")
    password = params.getvalue("password")
    success, user_id = auth.authenticate(username, password)
    if success:
        session_id = session.create_session()
        session.add_to_session({"user_id": user_id}, session_id=session_id)
        print ('Location: upload.py')

base.start_html()
print_login_form()
if (os.environ["REQUEST_METHOD"].upper() == "POST" and not success):
    print ("<div>Login Error</div>")
base.finish_html()