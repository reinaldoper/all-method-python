class MathUtils:
    @classmethod
    def calculate_average(cls, numbers):
        return sum(numbers) / len(numbers)

    @staticmethod
    def is_even(number):
        return number % 2 == 0


numbers_list = [1, 2, 3, 4, 5]
print("Média dos números:", MathUtils.calculate_average(numbers_list))

number = 6
if MathUtils.is_even(number):
    print(f"{number} é par.")
else:
    print(f"{number} é ímpar.")
