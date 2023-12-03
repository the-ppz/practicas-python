# Suma con funciones

"""
def sumarNumeros(a, b):
    suma = a + b
    print(f"La suma de {a} + {b} es {suma}")
"""

"""
def sumarNumeros():
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    suma = a + b
    print(f"La suma es: {a} + {b} = {suma}")
"""

def sumarNumeros():
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    return a + b

resultado = sumarNumeros()
print(f"La suma es {resultado}")

resultado += 10
print(f"El resultado + 10 a es {resultado}")