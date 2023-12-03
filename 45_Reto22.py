""" Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o 
superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales
y muestre por pantalla si el usuario tiene que tributar o no. """

edad = int(input("Ingrese su edad: "))
ingresos = float(input("Ingrese su sueldo: "))

if edad > 0 and edad < 90:
    if ingresos > 0:
        if edad > 16 and ingresos > 10000:
            print("Debes de pagar impuestos")
        else:
            print("No debes pagar impuestos")
    else:
        print("Tu ingreso tiene que ser mayor o igual que 0 dolares")
else:
    print("Edad no VALIDA")