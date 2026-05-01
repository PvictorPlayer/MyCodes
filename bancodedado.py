import sqlite3

print("Banco de dados")

conexao = sqlite3.connect("programaçao/banco.db")
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS contas_bancarias (
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               titular TEXT NOT NULL,
               saldo FLOAT NOT NULL,
               cpf TEXT NOT NULL UNIQUE
               )""")
# cursor.execute(f"""INSERT INTO contas_bancarias
#             (titular, saldo, cpf) VALUES
#             ('paulo', -3000, '92836134')""")

# cursor.execute("""INSERT INTO contas_bancarias
#                (titular, saldo, cpf) VALUES
#                ('pedro', 500, '2356235274293')""")

cursor.execute("""UPDATE contas_bancarias SET saldo = -5000 WHERE id = 2""")
cursor.execute("""SELECT titular, saldo FROM contas_bancarias""")
contas = cursor.fetchall()
for conta in contas:
    titular, saldo = conta
    print(f"""\ntitular: {titular}
saldo: {saldo}\n""")
conexao.commit()