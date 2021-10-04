#!C:\Python27\python.exe

import base
import cgi
import os
import auth

def print_logout_form():
    print (''' 
        <form method="POST">            
            <input type="submit" value="Logout"/>
        </form>
    ''')

params = cgi.FieldStorage()
if os.environ["REQUEST_METHOD"].upper() == "POST":
    auth.logout()
    print('Location: login.py')    

base.start_html()
print_logout_form()
base.finish_html()