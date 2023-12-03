# ZeroDivisionError
def division(a,b):
    try:
        r = a / b
        print(f"El resultado de la division es: {r}")
    except ZeroDivisionError:
        print("No se puede dividir entre cero")

    print("Continuar con el sistema")

respuesta = division(5,2)
print(respuesta)

# TypeError
def suma(a,b):
    try:
        r = a + b
        print(f"El resultado de la suma es: {r}")
    except TypeError:
        print("Uno de los valores no es un numero")

    print("Continuar con el sistema")


respuesta1 = suma(5,2)
print(respuesta1)