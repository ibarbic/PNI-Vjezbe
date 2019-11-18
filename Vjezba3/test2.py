#!C:\ProgramData\Anaconda3\python.exe

import cgi
params = cgi.FieldStorage()
ime = params.getvalue("ime")
lozinka = params.getvalue("lozinka")
r_lozinka =params.getvalue("r_lozinka")
print ('''
<!DOCTYPE html>
<html>
<head>
  ''')
if(r_lozinka != lozinka):
  print ('<meta http-equiv="refresh" content="0; url=http://localhost:8080/test/test1.py" />')
print('''  
</head>
<body>
<h2>Unesite podatke:</h2>
<form action="test3.py" method="post">
  Status:
  <input type="radio" name="status" value="redovni"> Redovni
  <input type="radio" name="status" value="izvanredni"> Izvanredni
  <br><br>
  E-mail: <input type="email" name="email">
  <br><br>
  <select name="smjer">
    <option value="programiranje">Programiranje</option>
    <option value="baze_podataka">Baze podataka</option>
    <option value="mreze">Mreze</option>
    <option value="informacijski_sustavi">Informacijski sustavi</option>
  </select>
  <br><br>
  <input type="checkbox" name="zavrsni" value="Da"> Zavrsni<br>
  ''')
print ('<input type="hidden" name="ime" value="' + ime + '">')
print ('<input type="hidden" name="lozinka" value="' + lozinka + '">')
print ('''
<br>
<input type="submit" value="Next">
</form>
</body>
</html>''')