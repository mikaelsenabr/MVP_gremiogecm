import sqlite3

conexao = sqlite3.connect("gremio.db")
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS membros (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cargo TEXT NOT NULL,
                idade INTEGER NOT NULL
                )""")