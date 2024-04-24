import mysql.connector

# Conectar ao banco de dados MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="python"
)


laravel = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="laravel",
)


array = [
  {
    "name": "torresmo",
    "quantity": 12,
    "price": 2.99,
    "fornecedor_id": 1
  },
  {
    "name": "ração animal",
    "quantity": 11,
    "price": 22.8,
    "fornecedor_id": 3
  },
  {
    "name": "frango assado",
    "quantity": 34,
    "price": 41.99,
    "fornecedor_id": 2
  },
  {
    "name": "bombril",
    "quantity": 12,
    "price": 1.99,
    "fornecedor_id": 2
  }
]