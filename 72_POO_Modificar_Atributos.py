# Modificar atributos o varios
"""
class Validando:
    def __init__(self):
        self.estado = False

    def cambiarTrue(self):
        self.estado = True

    def imprimirEstado(self):
        print(self.estado)

e = Validando()
e.imprimirEstado()
e.cambiarTrue()
e.imprimirEstado()
"""

# Ejercicio 2
class Articulo:
    def __init__(self,cod,cant,prec):
        self.codigo = cod
        self.cantidad = cant
        self.precio = prec

    def producto(self):
        print(f"Codigo {self.codigo}, existe la cantidad de {self.cantidad} y su precio es {self.precio}")

    def comprarProducto(self,x):
        self.cantidad += x
        print(f"Incremento de {self.cantidad}")

    def venderProducto(self,x):
        self.cantidad -= x
        print(f"Venta {self.cantidad}")

p1 = Articulo(123,10,1000)
p1.producto()
p1.comprarProducto(10)
p1.producto()
p1.venderProducto(5)
p1.producto()