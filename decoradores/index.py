def my_decorator(func):
    def wrapper():
        print("Algo está acontecendo antes da função ser chamada.")
        func()
        print("Algo está acontecendo depois da função ser chamada.")
        func()
    return wrapper


@my_decorator
def say_hello():
    print("Olá, eu sou o decorador!")


say_hello()


def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


@repeat(num_times=3)
def greet(name):
    print(f"Olá, {name}!")


greet("Alice")


class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"A função {self.func.__name__} foi chamada {self.num_calls} vezes.")
        return self.func(*args, **kwargs)


@CountCalls
def say_hello():
    print("Olá!")


say_hello()
say_hello()

