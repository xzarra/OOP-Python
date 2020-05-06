class Kucing:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __str__(self):
        return 'penjumlahan(%d, %d)' % (self.a,self.b)

    def __add__(self, other):
        return Kucing(self.a + other.a, self.b + other.b)

data1 = Kucing(3,2)
data2 = Kucing(5,-3)

print(data1 + data2)