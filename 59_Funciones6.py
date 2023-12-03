# Menu

def sumaNum():
    a = float(input("Ingresa el primer numero: "))
    b = float(input("Ingresa el segundo numero: "))

    suma = a + b
    print(f"\nLa suma es {suma}\n\n")


def restaNum():
    a = float(input("Ingresa el primer numero: "))
    b = float(input("Ingresa el segundo numero: "))

    resta = a - b
    print(f"\nLa resta es {resta}\n\n")


def multiplicacionNum():
    a = float(input("Ingresa el primer numero: "))
    b = float(input("Ingresa el segundo numero: "))

    mul = a * b
    print(f"\nLa multiplicacion es {mul}\n\n")

# Inicio de Menu
bandera = True
num = 1

while bandera == True:
    print("1 -- Suma de dos numeros")
    print("2 -- Resta de dos numeros")
    print("3 -- Multiplicacion de dos numeros")
    print("4 -- Salir del Programa")
    num = int(input("Seleccione una opcion: "))

    if  num == 1 or num == 2 or num == 3 or num == 4:
        if num == 1:
            sumaNum()
        elif num == 2:
            restaNum()
        elif num == 3:
            multiplicacionNum()
        else:
            print("\n\nHasta la proxima\n\n")
            bandera = False
    else:
        print("\n\nNo es una Opcion Valida, por favor seleccione una opcion del 1 al 4\n\n")