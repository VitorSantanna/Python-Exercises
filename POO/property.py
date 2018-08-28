




class Retangulo:
    def __init__(self, l, a):
        self._l = 0
        self._a = 0

    def _get_l(self):
        return self._l

    def _set_l(self, largura):
        if not(isinstance(largura, int) and (largura > 0)):
            raise ValueError("Número Incorreto")
        self._l = largura

    def _get_a(self):
        return self._a

    def _set_a(self, altura):
        if not (isinstance(altura, int) and (altura > 0)):
            raise ValueError("Número Inválido!")
        self._a = altura

    def _get_area(self):
        return self._a*self._l

    a = property(_get_a, _set_a)
    l = property(_get_l, _set_l)
    area = property(_get_area)




r = Retangulo()
r.a = 10
r.l = 10
print(r.area)

if __name__ == "__main__":
    pass