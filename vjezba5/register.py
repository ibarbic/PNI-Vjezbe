#!C:\Python27\python.exe

import base
import cgi
import os
import auth
import db

def print_registration_form():
    print (''' 
        <form method="POST">
            username <input type="text" name="username" required /><br>
            password <input type="password" name="password" required/><br>
            repeat password <input type="password" name="password_repeat" required/><br>
            email <input type="email" name="email" required/><br>
            secret question 
            <select name="secret_question">
                <option value="What is your childhood friends name?">What is your childhood friends name?</option>
                <option value="What is your dogs name?">What is your dogs name?</option>
                
            </select><br>
            secret answer <input type="text" name="secret_answer" required/><br>
            <input type="submit" value="Register"/>
        </form>
    ''')

registration_error = "Registration Error!"

params = cgi.FieldStorage()
if os.environ["REQUEST_METHOD"].upper() == "POST":
    username = params.getvalue("username")
    password = params.getvalue("password")
    password_repeat = params.getvalue("password_repeat")
    email = params.getvalue("email")
    secret_question = params.getvalue("secret_question")
    secret_answer = params.getvalue("secret_answer")
    

    validation_error = False
    success = False

    if password != password_repeat:
        registration_error += "<br>Passwords must match!"    
        validation_error = True

    if db.get_user_by_email(email) != None:
        registration_error += "<br>Email " + email + "already exists!"    
        validation_error = True

    if validation_error == False:
        success = auth.register(username, password, email, secret_question, secret_answer)
        if success:
            print('Location: login.py')

base.start_html()
print_registration_form()
if os.environ["REQUEST_METHOD"].upper() == "POST" and not success:
    print("<div>" + registration_error + "</div>")
base.finish_html()