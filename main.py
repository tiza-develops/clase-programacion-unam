class cuadro:
    def __init__ (self, lado):
        self.lado = lado
        self.peri = lado*4
        self.area = lado**2
        print(self.peri)
        print(self.area)

class rectangulo:
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
        self.peri = l1*2+l2*2
        self.area = l1*l2
        print(self.peri)
        print(self.area)

class triangulo:
    def __init__(self, l1,l2,l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.semi = (l1+l2+l3)/2
        self.peri = (l1+l2+l3)
        self.area = (self.semi*(self.semi-self.l1)*(self.semi-self.l2)*(self.semi-self.l3)) ** 0.5
        print(self.peri)
        print(self.area)
