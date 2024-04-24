# Abre um arquivo para escrita (cria um novo se não existir)
with open("exemplo.txt", "w") as arquivo:
    arquivo.write("Olá, mundo!\n")
    arquivo.write("Este é um exemplo de escrita em arquivo em Python.\n")


# Abre o arquivo para leitura
with open("exemplo.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        print(linha.strip())  # strip() remove espaços em branco e quebras de linha extras
        
frases = ['Python', 'JavaScript', 'HTML', 'CSS']

# Abre o arquivo para anexar (adicionar ao final)
with open("exemplo.txt", "a") as arquivo:
    for line in frases:
        arquivo.write(line + "\n")

    
print('--------------------------------')

try:
    arquivo = open("arquivo_inexistente.txt", "r")
    conteudo = arquivo.read()
    arquivo.close()
except FileNotFoundError:
    print("O arquivo não foi encontrado.")
except IOError:
    print("Ocorreu um erro ao tentar abrir o arquivo.")


print('----------------------------------------------------------------')

try:
    with open("exemplo.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
        arquivo.close()
except IOError:
    print("Ocorreu um erro ao tentar ler o arquivo.")
except Exception as e:
    print("Ocorreu um erro:", e)


print('----------------------------------------------------------------')

try:
    with open("exemplo.txt", "a") as arquivo:
        arquivo.write("Conteúdo a ser escrito no arquivo.")
except IOError:
    print("Ocorreu um erro ao tentar escrever no arquivo.")
except Exception as e:
    print("Ocorreu um erro:", e)
finally:
    print("Este bloco é sempre executado, independentemente de exceções.")


print("-----------------------------------------------")

# Abre o arquivo para leitura
with open("./exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
    