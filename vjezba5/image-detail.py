#!C:\Python27\python.exe

import cgi, os, sys, cgitb, base
import session
import cgitb; cgitb.enable()
import db
import datetime
import Cookie
import json


request = cgi.FieldStorage()
    
if (os.environ["REQUEST_METHOD"].upper() == "GET"):
    id = request.getvalue("id")
    if not id > 0:
        print ("Location: login.py")

    image = db.get_image_by_id(id)
    if image is None:
        print ("Location: login.py")
    
    http_cookies_str = os.environ.get('HTTP_COOKIE', '')
    cookie_object = Cookie.SimpleCookie(http_cookies_str)
    images_visited = cookie_object.get("images_visited").value if cookie_object.get("images_visited") else None

    if images_visited is None:
        print ("Location: login.py")
    else:
        images_visited_dictionary = json.loads(images_visited)

        if str(id) in images_visited_dictionary:
            last_visited_date = datetime.datetime.strptime(images_visited_dictionary[str(id)], '%Y-%m-%d %H:%M:%S.%f')
            current_date = datetime.datetime.now()
            date_result = current_date - last_visited_date
            datetime.timedelta(0, 8, 562000)
            minutes, seconds = divmod(date_result.days * 86400 + date_result.seconds, 60)
            
            if minutes >= 1440:
                images_visited_dictionary[str(id)] = str(datetime.datetime.now())
                cookie_object["images_visited"] = json.dumps(images_visited_dictionary)
                print (cookie_object.output()) #upisivanje cookie-a u header
                db.increase_image_counter_by_id(str(id))
        else:
            images_visited_dictionary[str(id)] = str(datetime.datetime.now())
            cookie_object["images_visited"] = json.dumps(images_visited_dictionary)
            print (cookie_object.output()) #upisivanje cookie-a u header
            db.increase_image_counter_by_id(str(id))


if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    id = request.getvalue("id-to-delete")
    if not id > 0:
        print ("Location: login.py")
    image = db.get_image_by_id(id)
    image_path = image[2]+image[6]
    os.remove(image_path)
    db.delete_image_by_id(id)
    print ("Location: upload.py")

base.start_html()
print ('<form method="POST">')
image_path = "../../vjezba5final/"+image[2]+"/"+image[6]
print('<img src="'+ image_path +'" width=100 height=200><br>')
print ('<input type="hidden" name="id-to-delete" value='+ id +' >')
print (image_path[26:27])
print ('<input type="submit" value="Delete"/>')
print ('</form>')

base.finish_html()