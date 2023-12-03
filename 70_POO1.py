# Class -> molde de la base

# Ejemplo 1
"""
class Auto:
    marca = "Hino"
    modelo = "AK 2014"
    placa = 456
    color = "Negro"

# Instanciar el Elemento
# Instanciar es crear un elemento de la clase
bus = Auto()
print(bus.marca)
print(bus.modelo)
print(bus.placa)
print(bus.color)
"""

# Ejemplo 2
"""
class PersonaUno:
    nombre = "Franklin"
    apellidoP = "Alvarez"
    apellidoM = "Guadalupe"

class PersonaDos:
    nombre = "Luis"
    apellidoP = "Guadalupe"
    apellidoM = "Saltos"

p1 = PersonaUno()
print(f"Nombre de la persona #01 {p1.nombre} {p1.apellidoP} {p1.apellidoM}")

p2 = PersonaDos()
print(f"Nombre de la persona #02 {p2.nombre} {p2.apellidoP} {p2.apellidoM}")

p3 = PersonaUno()
print(f"Nombre de la persona #03 {p3.nombre} {p3.apellidoP} {p3.apellidoM}")
"""

# Ejemplo 3
"""
class Auto:
    marca = ""
    modelo = ""
    color = ""
    llantas = ""
    faros = ""

a1 = Auto()
a1.marca = "Kia"
a1.modelo = "Lujo"
a1.color = "Negro"
a1.llantas = "Rin 16"
a1.faros = "Alojeno"

a2 = Auto()
a2.marca = "Ford"
a2.modelo = "Lujo"
a2.color = "Rojo"
a2.llantas = "Rin 15"
a2.faros = "Normales"

print(f"Primer auto es de la marca {a1.marca} modelo {a1.modelo} de color {a1.color} con llantas {a1.llantas} y faros {a1.faros}")
print(f"Segundo auto es de la marca {a2.marca} modelo {a2.modelo} de color {a2.color} con llantas {a2.llantas} y faros {a2.faros}")
"""

