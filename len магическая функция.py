class Abc:

    def __init__(self, *a):
        self.a = a

    def __len__(self, *a):
        return len(self.a)


abc = Abc(2, 3, 4, 5)
print(len(abc))

class Abcd:

    def __init__(self, *a):
        self.a = a

    def __len__(self, *a):
        return sum(self.a)


abcd = Abcd(2, 3, 4, 5)
print(len(abcd))

