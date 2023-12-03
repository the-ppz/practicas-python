num = 10
bandera = True

while bandera == True:
    n = int(input("Ingrese un numero del 1 al 20: "))
    if n > 0 and n < 20:
        if n == num:
            print("\nFelicidades, adivinaste el numero.\n\n\n")
            bandera = False
        elif n > num:
            print(f"El numero ingresado {n} es mayor que el numero por adivinar\n")
        elif n < num:
            print(f"El numero ingresado {n} es menor que el numero por adivinar\n")
    else:
        print("Ingrese un numero valido que cumpla con el rango.\n\n")