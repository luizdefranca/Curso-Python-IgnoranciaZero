import sqlite3

conn = sqlite3.connect('iz.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE nivel (
        nivel_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nivel_nome VARCHAR(30) NOT NULL,
        UNIQUE(nivel_nome)
);
""")

cursor.execute("""
CREATE TABLE usuario (
usuario_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
usuario_login VARCHAR(30),
usuario_senha VARCHAR(100),
usuario_nome VARCHAR(100),
usuario_email VARCHAR(100),
usuario_nivel INTEGER NOT NULL,
UNIQUE(usuario_login),
UNIQUE(usuario_email)
);
""")

cursor.execute("""
CREATE TABLE log (
log_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
log_data VARCHAR(30) NOT NULL,
log_evento VARCHAR(30) NOT NULL,
log_usuario VARCHAR(30) NOT NULL,
log_ip VARCHAR(20) NOT NULL
);
""")

cursor.execute("""
INSERT INTO nivel (nivel_nome) VALUES ("admin");
""")

cursor.execute("""
INSERT INTO nivel (nivel_nome) VALUES ("cliente");
""")

cursor.execute("""
INSERT INTO usuario (usuario_login, usuario_senha, usuario_nome, usuario_email, usuario_nivel) VALUES ("admin", "admin", "admin", "meuemail@email.com", 1);
""")

conn.commit()

conn.close()
