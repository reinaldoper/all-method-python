def my_generator():
    yield 1
    yield 2
    yield 3


gen = my_generator()
for value in gen:
    print(value)


def infinite_generator():
    num = 1
    while True:
        yield num
        num += 1


gen = infinite_generator()
for i in range(5):
    print(next(gen))


def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


gen = fibonacci_generator(10)
for value in gen:
    print(value)
