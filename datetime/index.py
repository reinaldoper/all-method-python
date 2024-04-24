import datetime

agora = datetime.datetime.now()
print("Data e hora atual:", agora)


data_especifica = datetime.date(2023, 5, 17)
print("Data específica:", data_especifica)


data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
print("Data formatada:", data_formatada)


data1 = datetime.datetime(2023, 5, 17)
data2 = datetime.datetime(2023, 5, 20)
diferenca = data2 - data1
print("Diferença entre as datas:", diferenca)


data_atual = datetime.datetime.now()
um_dia = datetime.timedelta(days=1)
um_dia_depois = data_atual + um_dia
print("Um dia depois:", um_dia_depois)
