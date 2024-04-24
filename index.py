def soma(a, b):
    return a + b


print(soma(4, 5))


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Exemplo de uso da classe Pessoa


pessoa1 = Pessoa("João", 30)
pessoa1.apresentar()  # Saída: Olá, meu nome é João e tenho 30 anos.


a = 2.8
b = 3

print(soma(a, b))


ARRAY = [
  "RJ",
  "MG",
  "SP"
]


def array_sum(array):
    obj = []
    arr = []
    
    lista = ["Maria", "Pedro"]
    lista.extend(array)
    lista.reverse()
    
    for i in range(len(array)):
        obj.append(array[i])

    for i in range(len(obj)):
        if obj[i] != "RJ":
            arr.append(obj[i])
     
    def calculate_remainder():
        return 5 % 2

    text = f"""Os estados são:  {arr[0]} e {arr[1]}.
    O retorno da função é: {calculate_remainder()}. {lista}"""
    print(text)


array_sum(ARRAY)


def calculate_remainder():
    return 5 % 2


print(calculate_remainder())
