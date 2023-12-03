# Herencia
"""
class Carro:
    def __init__(self, nom, mod, color, precio):
        self.nombre = nom
        self.modelo = mod
        self.color = color
        self.precio = precio

    def descripcion(self):
        print(f"Nombre: {self.nombre}, Modelo: {self.modelo}, Color: {self.color}, Precio: {self.precio}")

c1 = Carro("Versa", "2001", "Negro", "15 000")
c1.descripcion()

class Chevrolet(Carro):
    def __init__(self,nom,mod,color,precio):
        super().__init__(nom,mod,color,precio)

    def marca(self,marca):
        print(f"Nombre: {self.nombre}, Modelo: {self.modelo}, Color: {self.color}, Precio: {self.precio}, Marca {marca}")

    def seguro(self,seguro):
        if self.nombre == "Onix":
            print("El seguro de tu Onix es GRATUITO")
        else:
            print(f"El costo de tu seguro es: {seguro}")

c2 = Chevrolet("Aveo", "2022", "Blanco", "100 000")
c2.marca("Chevrolet")
c2.seguro(10000)

c2 = Chevrolet("Onix", "2022", "Blanco", "100 000")
c2.marca("Chevrolet")
c2.seguro(1000)
"""

# Ejemplo
"""
class Sonido:
    def __init__(self):
        pass

    def tono(self):
        print("Suena el Telefono")

class Video:
    def __init__(self):
        pass

    def video(self):
        print("Se toma el VIDEO")

    def foto(self):
        print("Se toma la FOTO")

class Smartphone(Sonido,Video):
    def __init__(self,precio):
        self.precio = precio

    def mostrarPrecio(self):
        print(f"El precio por el smarthphone es {self.precio}")

t1 = Smartphone(45000)
t1.tono()
t1.foto()
t1.mostrarPrecio()
"""

# Polimorfismo
class Persona:
    def __init__(self, nom,ap,am):
        self.nombre = nom
        self.apellidoP = ap
        self.apellidoM = am

    def descripcion(self, mensaje):
        print(f"Saludos {self.nombre} {self.apellidoP} {self.apellidoM}")
        print("Esto es del tipo PERSONA")

class Arquitecto(Persona):
    def __init__(self,nom,ap,am):
        super().__init__(nom,ap,am)

    def descripcion(self,mensaje):
        print(f"Saludos {self.nombre} {self.apellidoP} {self.apellidoM} y el mensaje es: {mensaje}")
        print("Esto es del tipo ARQUITECTO")

class Ingeniero(Persona):
    def __init__(self, nom, ap, am):
        super().__init__(nom, ap, am)

    def descripcion(self, mensaje):
        print(f"Saludos {self.nombre} {self.apellidoP} {self.apellidoM} y el mensaje es: {mensaje}")
        print("Esto es del tipo INGENIERO")

p1 = Arquitecto("Luis", "Cabrera", "Guadalupe")
p1.descripcion("ESTO ES EL POLIMORFISMO")

p2 = Ingeniero("Franklin", "Alvarez", "Guadalupe")
p2.descripcion("EXPERTO EN PYTHON")