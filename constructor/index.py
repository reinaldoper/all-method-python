class cachorro:
    # Inicialização da classe
    def __init__(self, nome, cor, idade, lista=[]):
        self.nome = nome
        self.cor = cor
        self.idade = idade
        self.lista = lista

    # Método para representação em string
    def __str__(self):
        return f"""
                Nome: {self.nome} - Cor: {self.cor} - Idade: {self.idade}.
                Lista: {self.lista}
                """

# Criando uma lista vazia


nomes_cachorros = []

# Criando instâncias da classe cachorro e adicionando à lista
dog1 = cachorro("Luckily", "Red", 4, nomes_cachorros)
dog2 = cachorro("Buddy", "Brown", 2, nomes_cachorros)

# Adicionando nomes de cachorros à lista
nomes_cachorros.append(dog1.nome)
nomes_cachorros.append(dog2.nome)

# Imprimindo os nomes dos cachorros na lista
print("Nomes dos cachorros:", nomes_cachorros)
print(dog1)
print(dog2)
