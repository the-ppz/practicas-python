def sumarNumeros():
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))

    if a > 0 and b > 0:
        suma = a + b
        resta = a - b
        multiplicacion = a * b
        return suma, resta, multiplicacion # nos devuelve una tupla

resultado = sumarNumeros()
print(f"El resultado de las operaciones es {resultado}")

# Impresion de la Tupla
for num in resultado:
    print(num)

# Version 2
print("\n\n")
resultadoSuma, resultadoResta, resultadoMultiplicacion = sumarNumeros()
print(f"El resultado de la suma es {resultadoSuma}")
print(f"El resultado de la resta es {resultadoResta}")
print(f"El resultado de la multiplicacion es {resultadoMultiplicacion}")