import sqlite3
import os
print(os.path.join(os.getcwd(), 'iz.db'))
conn = sqlite3.connect(os.path.join(os.getcwd(), 'iz.db'))

cursor = conn.cursor()

cursor.execute("""
SELECT * FROM usuario WHERE usuario_login = 'admin' AND usuario_senha = 'admin'
""")
