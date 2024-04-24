class dicionario():
    def __init__(self, array: dict) -> None:
        self.array = array
      
    def implementation(self):
        for key, value in self.array.items():
            print(f"{key} = {value}")
            
    def value_msg(self):
        return self.array.get("pedro", {"error": "Invalid"})
            
    def __str__(self):
        return str(self.array)
      
      
array = {"nome": "Marcos", "idade": "21", "local": "Dourados"}


arr = dicionario(array)
arr.implementation()
print("Chaves do dicionário:", arr)
print(arr.value_msg())
