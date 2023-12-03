# Mayor de dos numeros

def numMayor(a,b):
    if(type(a) == int or type(a) == float):
        if (type(b) == int or type(b) == float):
            if a > b:
                print(f"El mayor es {a}")
                return a
            elif a == b:
                print("Los dos numeros son iguales")
                return a
            else:
                print(f"El mayor es {b}")
                return b
        else:
            print(f"El numero {b} no es un numero entero o flotante")
            return False
    else:
        print(f"El numero {a} no es un numero entero o flotante")
        return False

mayor = numMayor(45,54)
print(mayor)