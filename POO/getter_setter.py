#coding: utf-8

#author = "João Vitor de Araujo"
from typing import Any




class Retangulo():
    def __init__(self):
        self.l = 0
        self.a = 0

    def set_l(self, l):
        if not(isinstance(l, int) and (l>0)):
            raise ValueError("Número Incorreto")
        self.l = l

    def set_a(self, a):
        self.a = a
        if not (isinstance(a, int) and (a > 0)):
            raise ValueError("Número Inválido!")
        self.a = a

    def get_area(self):
        return self.l * self.a


r1 = Retangulo()
r1.set_l(10)
r1.set_a(10)
print(r1.get_area())

if __name__ == "__main__":
    pass






