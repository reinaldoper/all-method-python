class InfiniteIterator:
    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        self.num += 1
        return self.num


infinite_iter = InfiniteIterator()
for i in infinite_iter:
    print(i)
    if i >= 10:
        break
      
      
class SquareIterator:
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max_num:
            self.current += 1
            return self.current ** 2
        else:
            raise StopIteration


square_iter = SquareIterator(5)
for item in square_iter:
    print(item)

