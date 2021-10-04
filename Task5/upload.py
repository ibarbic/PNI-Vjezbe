#!C:\Python27\python.exe

import cgi, os, sys, cgitb, base
import session
import cgitb; cgitb.enable()
import db
import random

try: # Windows needs stdio set for binary mode.
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    pass


path = 'images/'
 
form = cgi.FieldStorage()

data = session.get_session_data()
if data is None:
    print ("Location: login.py")

else:
    user = db.get_user_by_id(str(data['user_id']))
    if user is None:
        print ("Location: login.py")
    
base.start_html()
if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    directory = form.getvalue("directory_name")
    file_item = form["avatar"]

    path += directory+"/"

    if not os.path.isdir(path):
        os.mkdir(path)

    if (file_item.filename):
        print("<br>")
        
    else:
        print ("<br>")
    
    if file_item.filename:
        filename, file_extension = os.path.splitext(file_item.filename)
        generated_name = str(random.randrange(100000000)) + file_extension
        fn = path
        fn += os.path.basename(generated_name)                
        #fn += os.path.basename(file_item.filename)
        open(fn, 'wb').write(file_item.file.read())
        message = 'The file "' + fn + '" was uploaded successfully'
        db.create_image(file_item.filename, path, generated_name)
        
    else:
        message = "No file was uploaded"
    

for directory_path, directory_names, image_names in os.walk('images/'):
    directories = directory_names
    images = image_names
    break
#print(path)
print('<form enctype="multipart/form-data" method="POST">')
print ('<input type="text"  name="newdir">')
dirname=form.getvalue("newdir")
if dirname:
    if dirname not in directories:
        os.mkdir("images/" +dirname)
print('<input type="submit" value="create" >')
print ("<br>")
print("Collection")
print ("<select name='directory_name'>")
for i in range(len(directory_names)):
    print("<option value='"+ directory_names[i] +"'>"+ directory_names[i] +"</option>")
print ("</select>")

print ("<br>")
print ('<input type="file"  name="avatar" accept="image/png, image/jpeg">')
print('<input type="submit" value="upload">')
print ('</form>')
print ("<a href='Logout.py'>Logout</a>")
images = db.get_images()
for image in images:
    image_path = "../../vjezba5final/"+image[2]+"/"+image[6]    
    print ('<div>')
    print('<a href="image-detail.py?id='+str(image[0])+'"><img src="'+ image_path +'" width=100 height=200></a><br>')
    
    if user[6] == 1:
        print ("times seen:" + str(image[3]))
    print ('</div>')

base.finish_html()