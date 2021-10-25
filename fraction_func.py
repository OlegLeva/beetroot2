class Fraction:
    def __init__(self, n, d):
        self.n = n
        self.d = d

    def evclid(self, n, d):
        while n % d != 0:
            oldn = n
            oldd = d
            n = oldd
            d = oldn % oldd
        return d

    def __add__(self, other):
        self.n = self.n * other.d + other.n * self.d
        self.d = self.d * other.d
        m = self.evclid(self.n, self.d)
        self.n /= m
        self.d /= m
        return Fraction(self.n, self.d)


    def __repr__(self):
        return "{}/{}".format(int(self.n), int(self.d))


a = Fraction(3, 9)
b = Fraction(9, 81)

print(a+b)

