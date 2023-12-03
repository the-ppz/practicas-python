# Constructor
"""
class Ropa:
    def __init__(self): #Constructor
        self.marca = "Marca1"
        self.talla = "Mediana"
        self.color = "Negro"

r1 = Ropa()
print(f"Marca: {r1.marca}")
print(f"Talla: {r1.talla}")
print(f"Color: {r1.color}")

print("\n******************************\n")

r2 = Ropa()
r2.marca = "Jordan"
print(f"Marca: {r2.marca}")
print(f"Talla: {r2.talla}")
print(f"Color: {r2.color}")
"""

# Ejemplo 1 Constructores
"""
class Operaciones:
    def __init__(self,a,b):
        self.suma = a + b
        self.resta = a - b
        self.multiplicacion = a * b
        self.division = a / b

op1 = Operaciones(20,5)
print(f"La suma es {op1.suma}")
print(f"La resta es {op1.resta}")
print(f"La multiplicacion es {op1.multiplicacion}")
print(f"La division es {op1.division}")
"""

# Ejercicio 2
"""
class Operaciones:
    def __init__(self,a,b):
        self.num1 = a
        self.num2 = b
        self.resta = self.num1 - self.num2

    def resultadoSuma(self):
        print(f"La suma es {self.num1 + self.num2}")

    def resultadoResta(self):
        print(f"La resta es {self.resta}")

op1 = Operaciones(10,5)
op1.resultadoSuma()
op1.resultadoResta()
"""

# Ejercicio 3
class Persona:
    def __init__(self,nom,edad,tel):
        self.nombre = nom
        self.edad = edad
        self.telefono = tel

    def imprimir(self):
        print(f"Bienvenido {self.nombre} tienes {self.edad} anios y su telefono es 0{self.telefono}")

    def comentario(self,texto):
        print(f"La persona {self.nombre} nos dice {texto}")

p1 = Persona("Franklin",22,985625075)
p1.imprimir()
p1.comentario("Saludos desde Ecuador")