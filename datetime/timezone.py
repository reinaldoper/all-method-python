import datetime
import pytz

# Define a data e hora atual sem informação de fuso horário
data_atual = datetime.datetime.now()

# Define um objeto de fuso horário específico (UTC neste caso)
fuso_horario_utc = pytz.utc

# Adiciona informação de fuso horário à data atual
data_utc = data_atual.replace(tzinfo=fuso_horario_utc)

# Converte a data para outro fuso horário (Londres neste caso)
fuso_horario_londres = pytz.timezone('Europe/London')
data_londres = data_utc.astimezone(fuso_horario_londres)

# Imprime as datas e fusos horários
print("Data e hora em UTC:", data_utc.strftime('%Y-%m-%d %H:%M:%S %Z%z'))
print("Data e hora em Londres:", data_londres.strftime('%Y-%m-%d %H:%M:%S %Z%z'))
