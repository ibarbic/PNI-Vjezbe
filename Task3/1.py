#!C:/Users/ivanb/Anaconda3/python.exe
import cgi
import os
import cgitb
cgitb.enable(display=0, logdir="")

print  ("""
<!DOCTYPE html>
<html>
<body>
<h2>Unesite podatke:</h2>
<form action="2.py" method="post">
  Ime:
  <input type="text" name="ime" value="">
  <br><br>
  Lozinka:
  <input type="password" name="lozinka">
  <br><br>
  Ponovi lozinku:
  <input type="password" name="r_lozinka">
  <br><br>
  <input type="submit" value="Next">
</form> 


</body>
</html>
""")



