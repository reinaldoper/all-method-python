class Pai1:
    def __init__(self, name):
        self.name = name
    
    def metodo_pai1(self):
        print(self.name)


class Pai2:
    def __init__(self, idade):
        self.idade = idade
    
    def metodo_pai2(self):
        print(self.idade)


class Filho(Pai1, Pai2):
    def __init__(self, name, idade):
        Pai1.__init__(self, name)
        Pai2.__init__(self, idade)

    def metodo_filho(self):
        print("Método do Filho")


objeto_filho = Filho("Joao", 39)

objeto_filho.metodo_filho()
objeto_filho.metodo_pai1()
objeto_filho.metodo_pai2()
