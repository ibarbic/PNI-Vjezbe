#!C:\Python27\python.exe

import base

def print_menu():
    print ("<a href='login.py'>Login</a>")
    print ("<br>")
    print ("<a href='register.py'>Register</a>")
    print ("<br>")
    print ("<a href='upload.py'>Upload</a>")
    print("<br>")
    print ("<a href='password_change.py'>Password change</a>")

base.start_html()
print_menu()
base.finish_html()