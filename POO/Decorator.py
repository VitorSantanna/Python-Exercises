
class Retangulo:
    def __init__(self, l, a):
        self._l = 0
        self._a = 0
        self.l = l
        self.a = a

    @property
    def l(self):
        return self._l

    @l.setter
    def l(self, largura):
        if not(isinstance(largura, int) and (largura > 0)):
            raise ValueError("Número Incorreto")
        self._l = largura

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, altura):
        if not(isinstance(altura, int) and (altura > 0)):
            raise ValueError("Número Inválido!")
        self._a = altura

    @property
    def area(self):
        return self.a*self.l


r = Retangulo(20, 30)

print(r.area)

if __name__ == "__main__":
    pass
