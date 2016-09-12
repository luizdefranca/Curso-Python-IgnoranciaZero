#!/usr/bin/python
import cgitb; cgitb.enable()

print('Content-type: text/html\n')
print("""
<html>
<body>
   <form enctype="multipart/form-data" action="save_file.py" method="post">
   <p>Arquivo: <input type="file" name="filename" /></p>
   <p><input type="submit" value="Enviar" /></p>
   </form>
</body>
</html>
"""
)
