def my_tuples(name: str) -> tuple:
    texto = ("Laranja", "Maça", "Uva",)

    dupla = list(texto)
    my_text = []
    dupla.append(name)

    for i in range(len(texto)):
        print(texto[i])

    for index, text in enumerate(texto):
        print(f"{index + 1}: {text}")

    for index, text in enumerate(dupla):
        my_text.append({
            index + 1: text
        })

    for index, text in enumerate(my_text):
        print(f"{text}")

    print(my_text)


my_tuples("Joao")
