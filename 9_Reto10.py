peso_payaso = 112
peso_muneca = 75

numero_payasos = int(input("Dame el numero de Payasos a enviar: "))
numero_munecas = int(input("Dame el numero de Muniecas a enviar: "))

total_payasasos = peso_payaso * numero_payasos
total_munecas = peso_muneca * numero_munecas

total = total_munecas + total_payasasos

print("El peso total es: " + str(round(total,2)))