# Suma Predefinida
"""
def sumarNumeros(a,b):
    return a + b

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

resultado = sumarNumeros(num1, num2)

print(f"La suma de los dos numeros es {resultado}")
"""

# Funciones Predefinidas
"""
def division(a,b):
    return divmod(a,b) # funcion que devuelve (cociente, residuo)

operacion = division(10,5)
print(f"La division es {operacion}")
"""

# Mayor de n numeros

def mayorNum(a,b,c,d):
    mayor = max(a,b,c,d)
    return mayor

def menorNum(a,b,c,d):
    menor = min(a,b,c,d)
    return menor

resultado = mayorNum(3,4,5,6)
resultado2 = menorNum(3,4,5,6)
print(f'El mayor es {resultado}')
print(f'El menor es {resultado2}')