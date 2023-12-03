nombre = input("Dame tu nombre: ")
horas = float(input("Dame el numero de horas que trabajaste: "))
pago = float(input("Cuanto te pagan por hora: "))

total = horas * pago

print("Saludos " + nombre + " tu pago es: " + str(total))