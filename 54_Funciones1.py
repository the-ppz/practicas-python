"""
def saludo():
    print("Hola, Frank, bienvenido")

saludo()
saludo()
"""

# Funciones por Parametros
def saludar(nom, ape, an):
    print(f"\n\nHola, {nom} {ape}, bienvenido.")
    print(f"Tienes {an} anios de edad.\n\n")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
anios = int(input("Ingrese su anios: "))

saludar(nombre, apellido, anios)