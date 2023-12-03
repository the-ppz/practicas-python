# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

num = int(input("Ingrese un numero entero entre 1 y 1000: "))

if num > 0 and num <= 1000:
    print("BIENVENIDO")
    if num % 2 == 0:
        print(f"El numero {num} es par")
    else:
        print(f"El numero {num} es impar")
else:
    print("Numero entero no valido")