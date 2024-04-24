class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Duck(Animal):
    def speak(self):
        return "Quack!"


def make_animal_speak(animal):
    return animal.speak()


dog = Dog()
cat = Cat()
duck = Duck()

print("O cachorro diz:", make_animal_speak(dog))
print("O gato diz:", make_animal_speak(cat))
print("O pato diz:", make_animal_speak(duck))
