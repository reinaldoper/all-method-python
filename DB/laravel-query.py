import db

laravel = db.laravel.cursor()

query_laravel = 'SELECT name, COUNT(*) FROM Users group by name'

payments_query = 'SELECT status, currency FROM PaymentRequest'

laravel.execute(query_laravel)

listar = []
for item in laravel.fetchall():
    listar.append(set(item))

for dicionario in listar:
    for valor in dicionario:
        print(valor)
 
print('----------------------------------------------------------------')

laravel.execute(payments_query)

listar_payment = []
for item in laravel.fetchall():
    listar_payment.append(set(item))

for dicionario in listar_payment:
    for index, valor in enumerate(dicionario):
        print(index, valor)
