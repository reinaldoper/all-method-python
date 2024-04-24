class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("O raio deve ser um valor positivo.")
        self._radius = value

    @property
    def diameter(self):
        return 2 * self._radius

    @property
    def area(self):
        return 3.14 * self._radius ** 2


circle = Circle(5)
print("Raio:", circle.radius)
print("Diâmetro:", circle.diameter)
print("Área:", circle.area)


circle.radius = 7
print("Novo raio:", circle.radius)
print("Novo diâmetro:", circle.diameter)
print("Nova área:", circle.area)
