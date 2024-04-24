class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        print("Som genérico de animal")


class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca

    def fazer_som(self):
        print("Au au!")

    def abanar_rabo(self):
        texto = f"Orabo do cachorro {self.raca} esta abanando."
        print(texto)


meu_cachorro = Cachorro("Rex", "Labrador")
print(meu_cachorro.nome)
print(meu_cachorro.raca)
meu_cachorro.fazer_som()
meu_cachorro.abanar_rabo()
