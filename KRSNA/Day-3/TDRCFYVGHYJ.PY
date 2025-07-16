class Counter:
    def __init__(self, limit):
        self.limit = limit

    def count_up(self):
        for i in range(1, self.limit + 1):
            print(i, end=' ')

c = Counter(3)
c.count_up()