import db
import csv
from openpyxl import Workbook


cursor = db.conn.cursor()

result = db.conn.cursor()

nova = db.conn.cursor()

laravel = db.laravel.cursor()

query_laravel = 'SELECT name, COUNT(*) FROM users group by name'

laravel.execute(query_laravel)

listar = []
for item in laravel.fetchall():
    listar.append(set(item))
    
for dicionario in listar:
    for valor in dicionario:
        print(valor)


# Exemplo de consulta
query = "SELECT * FROM produtos c order by c.name ASC"
cursor.execute(query)

obj = []
for row in cursor.fetchall():
    obj.append(row)

consulta = """
  SELECT p.name AS product_name, COUNT(*) AS count
  FROM produtos p
  INNER JOIN fornecedor f ON p.fornecedor_id = f.id
  GROUP BY p.name;

"""
result.execute(consulta)

new_consulta = """
  SELECT COUNT(*) from client c inner join fornecedor f
  WHERE c.id = f.client_id
"""

for row in result.fetchall():
    print(row)

cursor.close()
result.close()
# insert.close()

nova.execute(new_consulta)

print('\n================================')
for row in nova.fetchall():
    print(row)


db.conn.close()


print('\n================================')

nome_arquivo = 'dados.csv'

with open(nome_arquivo, 'w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    for linha in obj:
        escritor_csv.writerow(linha)

print(f'O arquivo CSV "{nome_arquivo}" foi criado com sucesso.')

wb = Workbook()

# Selecionar a planilha ativa
ws = wb.active

# Preencher os dados na planilha
for linha in obj:
    ws.append(linha)

# Salvar o arquivo Excel
nome_arquivo_excel = 'dados.xlsx'
wb.save(nome_arquivo_excel)

print(f'O arquivo Excel "{nome_arquivo_excel}" foi criado com sucesso.')


print("--------------------------------")

objs = []


def read_arq(arq_file):
    with open('./dados.csv', 'r') as ficheiro:
        reader = csv.reader(ficheiro)

        for index, linha in enumerate(reader):
            objs.append({f"index {index + 1}": linha[1]})
    index = 0
    for linha in arq_file:
        index += 1
        print(linha['index' + f" {index}"])


read_arq(objs)
