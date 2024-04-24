import csv

# Dados a serem escritos no arquivo CSV
dados_novos = [
    ["Nome", "Idade", "Cidade"],
    ["João", 30, "São Paulo"],
    ["Maria", 25, "Rio de Janeiro"],
    ["Pedro", 35, "Belo Horizonte"]
]

# Escreve os dados_novos no arquivo CSV
with open("dados_novos.csv", "w", newline="") as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerows(dados_novos)


# Lê os dados_novos do arquivo CSV
try:
    with open("dados_novos.csv", "r") as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        for linha in leitor:
            print(linha)
except Exception as e:
    print("Ocorreu um erro:", e)

# Lê os dados_novos do arquivo CSV com cabeçalhos
with open("dados_novos.csv", "r") as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv)
    for linha in leitor:
        print(linha["Nome"], linha["Idade"], linha["Cidade"])