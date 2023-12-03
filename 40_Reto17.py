# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

nombre = input('Ingrese su nombre: ')
edad = int(input("Ingrese su edad: "))

if edad > 0 and edad < 100:
    if edad >= 18:
        print(f"Hola {nombre} eres es mayor de edad. Tienes {edad} anios.")
    else:   
        print(f"Hola {nombre} eres es menor de edad. Tienes {edad} anios.")
else:
    print("No es una edad valida. Introdue una edad de 1 a 100 anios")