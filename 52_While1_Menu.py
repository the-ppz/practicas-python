# Ciclo While
# Menu con 2 Operaciones

# Version 1.0
'''
num = 0

while num != 3:
    a = 0
    b = 0
    print("1 - Suma de dos numeros")
    print("2 - Resta de dos numeros")
    print("3 - Salir")
    num = int(input("Seleccione una opcion: "))

    if num == 1:
        a = float(input("Ingrese el primer numero: "))
        b = float(input("Ingrese el segundo numero: "))
        suma = a + b
        print(f"La suma de los dos numeros es {suma}")
    elif num == 2:
        a = float(input("Ingrese el primer numero: "))
        b = float(input("Ingrese el segundo numero: "))
        resta = a - b
        print(f"La resta de los dos numeros es {resta}")
    else:
        print("Hasta Luego")
'''

# Vesion 2.0
'''
num = 0

while num != 3:
    a = 0
    b = 0
    print("1 - Suma de dos numeros")
    print("2 - Resta de dos numeros")
    print("3 - Salir")
    num = int(input("Seleccione una opcion: "))

    if num == 1 or num == 2 or num == 3:
        if num == 1:
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
            suma = a + b
            print(f"La suma de los dos numeros es {suma}")
        elif num == 2:
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
            resta = a - b
            print(f"La resta de los dos numeros es {resta}")
        else:
            print("\nHasta Luego")
    else:
        print("\nIngrese un numero correcto.")
'''

# Vesion 3.0 CON BANDERAS
num = 0
bandera = True

while bandera == True:
    a = 0
    b = 0
    print("1 - Suma de dos numeros")
    print("2 - Resta de dos numeros")
    print("3 - Salir")
    num = int(input("Seleccione una opcion: "))

    if num == 1 or num == 2 or num == 3:
        if num == 1:
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
            suma = a + b
            print(f"La suma de los dos numeros es {suma}")
        elif num == 2:
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
            resta = a - b
            print(f"La resta de los dos numeros es {resta}")
        else:
            print("\nHasta Luego")
            bandera = False
    else:
        print("\nIngrese un numero correcto.")
